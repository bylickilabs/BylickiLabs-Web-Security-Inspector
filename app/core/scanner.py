from __future__ import annotations

import socket
import time
import warnings
from datetime import datetime, timezone
from typing import Callable
from urllib.parse import urlparse

import requests
import urllib3

from app.config import APP_VERSION, MAX_RESPONSE_BYTES, USER_AGENT
from app.core.settings import AppSettings
from app.core.validation import normalize_url
from app.models import Finding, ScanMetrics, ScanResult
from app.scanners.content import scan_content
from app.scanners.cookies import scan_cookies
from app.scanners.cors import scan_cors
from app.scanners.dns_scan import scan_dns
from app.scanners.external import run_observatory, run_pagespeed
from app.scanners.forms import scan_forms
from app.scanners.http_headers import scan_headers
from app.scanners.methods import scan_methods
from app.scanners.performance import collect_response_samples
from app.scanners.resources import scan_resources
from app.scanners.tls_scan import scan_tls

LogCallback = Callable[[str], None]
ProgressCallback = Callable[[int, str], None]


class WebsiteScanner:
    def __init__(
        self,
        settings: AppSettings,
        log_callback: LogCallback | None = None,
        progress_callback: ProgressCallback | None = None,
    ) -> None:
        self.settings = settings
        self.log_callback = log_callback or (lambda message: None)
        self.progress_callback = progress_callback or (lambda value, message: None)
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,application/json;q=0.8,*/*;q=0.5"})

    def _log(self, message: str) -> None:
        self.log_callback(message)

    def _progress(self, value: int, message: str) -> None:
        self.progress_callback(value, message)
        self._log(message)

    def scan(self, target: str, profile: str = "Standard") -> ScanResult:
        url = normalize_url(target)
        started = datetime.now(timezone.utc)
        timer = time.perf_counter()
        findings: list[Finding] = []
        metrics = ScanMetrics()
        parsed = urlparse(url)
        host = parsed.hostname or ""
        timeout = int(self.settings.timeout_seconds)
        verify_tls = bool(self.settings.verify_tls)

        if not verify_tls:
            warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)

        self._progress(3, f"Initialising {profile} assessment for {url}")
        request_start = time.perf_counter()
        response = self.session.get(
            url,
            timeout=timeout,
            verify=verify_tls,
            allow_redirects=True,
            stream=True,
        )
        metrics.response_time_ms = round((time.perf_counter() - request_start) * 1000, 3)
        content = response.raw.read(MAX_RESPONSE_BYTES, decode_content=True)
        response.close()
        text = content.decode(response.encoding or "utf-8", errors="replace")
        final_url = response.url
        final_parsed = urlparse(final_url)
        headers = dict(response.headers)
        metrics.status_code = response.status_code
        metrics.final_url = final_url
        metrics.response_size_bytes = len(content)
        metrics.redirect_count = len(response.history)
        metrics.metadata["redirect_chain"] = [
            {"status": item.status_code, "url": item.url, "location": item.headers.get("Location", "")}
            for item in response.history
        ]
        metrics.metadata["http_version"] = {10: "HTTP/1.0", 11: "HTTP/1.1", 20: "HTTP/2"}.get(
            getattr(response.raw, "version", 0), "Unknown"
        )
        metrics.checks_executed += 1

        self._progress(12, "Analysing response headers and redirect behaviour")
        findings.extend(scan_headers(final_url, headers, final_parsed.scheme == "https"))
        if parsed.scheme == "http" and final_parsed.scheme != "https":
            findings.append(
                Finding(
                    category="Transport Security",
                    title="HTTP does not redirect to HTTPS",
                    severity="High",
                    confidence="High",
                    description="The requested HTTP address did not transition to an encrypted HTTPS endpoint.",
                    evidence=final_url,
                    remediation="Redirect all HTTP traffic to HTTPS and enable HSTS after validation.",
                    url=url,
                    cwe="CWE-319",
                )
            )
        metrics.checks_executed += 2

        self._progress(22, "Reviewing cookies, page content and forms")
        raw_headers = getattr(response.raw, "headers", None)
        if raw_headers and hasattr(raw_headers, "getlist"):
            set_cookie_headers = raw_headers.getlist("Set-Cookie")
        else:
            set_cookie_headers = [response.headers.get("Set-Cookie", "")]
        findings.extend(scan_cookies(final_url, set_cookie_headers))
        content_findings, content_metadata = scan_content(final_url, text)
        findings.extend(content_findings)
        findings.extend(scan_forms(final_url, text))
        metrics.metadata.update(content_metadata)
        metrics.checks_executed += 3

        self._progress(34, "Resolving DNS and mail security records")
        dns_findings, dns_records, dns_ms = scan_dns(host, final_url)
        findings.extend(dns_findings)
        metrics.dns_time_ms = round(dns_ms, 3)
        metrics.metadata["dns_records"] = dns_records
        try:
            metrics.metadata["resolved_addresses"] = sorted({item[4][0] for item in socket.getaddrinfo(host, None)})
        except socket.gaierror:
            metrics.metadata["resolved_addresses"] = []
        metrics.checks_executed += 1

        if final_parsed.scheme == "https":
            self._progress(46, "Inspecting TLS certificate and negotiated protocol")
            tls_findings, tls_metadata, tls_ms = scan_tls(
                final_parsed.hostname or host,
                final_parsed.port or 443,
                final_url,
                timeout,
            )
            findings.extend(tls_findings)
            metrics.tls_time_ms = round(tls_ms, 3)
            metrics.metadata["tls"] = tls_metadata
            metrics.checks_executed += 1

        if profile in {"Standard", "Extended"}:
            self._progress(58, "Validating CORS and HTTP method configuration")
            probe_origin = "https://security-check.invalid"
            try:
                cors_response = self.session.options(
                    final_url,
                    headers={
                        "Origin": probe_origin,
                        "Access-Control-Request-Method": "GET",
                        "User-Agent": USER_AGENT,
                    },
                    timeout=timeout,
                    verify=verify_tls,
                    allow_redirects=True,
                )
                findings.extend(scan_cors(final_url, dict(cors_response.headers), probe_origin))
                metrics.metadata["cors_status"] = cors_response.status_code
            except requests.RequestException as exc:
                metrics.metadata["cors_error"] = str(exc)
            method_findings, method_metadata = scan_methods(final_url, self.session, timeout, verify_tls)
            findings.extend(method_findings)
            metrics.metadata.update(method_metadata)
            metrics.checks_executed += 2

        if profile == "Extended":
            self._progress(69, "Checking common public resources and deployment artefacts")
            resource_findings, resource_statuses = scan_resources(final_url, self.session, timeout, verify_tls)
            findings.extend(resource_findings)
            metrics.metadata["resource_statuses"] = resource_statuses
            metrics.checks_executed += len(resource_statuses)

        self._progress(79, "Collecting response time samples for statistical analysis")
        metrics.response_samples_ms = collect_response_samples(
            final_url,
            self.session,
            timeout,
            verify_tls,
            self.settings.sample_count,
        )
        metrics.checks_executed += len(metrics.response_samples_ms)

        if self.settings.enable_observatory:
            self._progress(86, "Querying MDN HTTP Observatory")
            findings.extend(run_observatory(final_url, timeout))
            metrics.checks_executed += 1

        if self.settings.enable_pagespeed:
            self._progress(92, "Querying Google PageSpeed Insights")
            page_findings, page_scores = run_pagespeed(
                final_url,
                self.settings.pagespeed_api_key,
                timeout,
            )
            findings.extend(page_findings)
            metrics.pagespeed_scores = page_scores
            metrics.checks_executed += 1

        completed = datetime.now(timezone.utc)
        result = ScanResult(
            target=url,
            profile=profile,
            findings=findings,
            metrics=metrics,
            started_at=started.isoformat(),
            completed_at=completed.isoformat(),
            duration_seconds=round(time.perf_counter() - timer, 3),
            application_version=APP_VERSION,
        )
        self._progress(100, f"Assessment completed with {len(findings)} findings")
        return result
