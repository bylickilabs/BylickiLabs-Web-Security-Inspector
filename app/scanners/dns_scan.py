from __future__ import annotations

import time
import ipaddress

import dns.exception
import dns.resolver

from app.models import Finding
from app.scanners.common import finding


def _resolve(resolver: dns.resolver.Resolver, name: str, record_type: str) -> list[str]:
    try:
        answer = resolver.resolve(name, record_type, lifetime=5)
        return [item.to_text() for item in answer]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
        return []


def scan_dns(host: str, url: str) -> tuple[list[Finding], dict[str, list[str]], float]:
    start = time.perf_counter()
    try:
        address = ipaddress.ip_address(host)
        records = {"A": [str(address)] if address.version == 4 else [], "AAAA": [str(address)] if address.version == 6 else [], "MX": [], "NS": [], "TXT": [], "CAA": [], "DMARC": []}
        return [], records, (time.perf_counter() - start) * 1000
    except ValueError:
        pass
    if host.lower() == "localhost":
        records = {"A": ["127.0.0.1"], "AAAA": ["::1"], "MX": [], "NS": [], "TXT": [], "CAA": [], "DMARC": []}
        return [], records, (time.perf_counter() - start) * 1000
    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 5
    records = {
        record_type: _resolve(resolver, host, record_type)
        for record_type in ("A", "AAAA", "MX", "NS", "TXT", "CAA")
    }
    records["DMARC"] = _resolve(resolver, f"_dmarc.{host}", "TXT")
    elapsed_ms = (time.perf_counter() - start) * 1000
    results: list[Finding] = []

    if not records["CAA"]:
        results.append(
            finding(
                "DNS",
                "CAA record not detected",
                "Low",
                "No Certificate Authority Authorization record was found.",
                host,
                "Consider defining which certificate authorities may issue certificates for the domain.",
                url,
                confidence="High",
            )
        )
    if len(records["NS"]) == 1:
        results.append(
            finding(
                "DNS",
                "Single authoritative nameserver detected",
                "Medium",
                "Only one nameserver record was returned, reducing DNS resilience.",
                records["NS"][0],
                "Use multiple authoritative nameservers on independent infrastructure.",
                url,
                confidence="High",
            )
        )
    spf_records = [value for value in records["TXT"] if "v=spf1" in value.lower()]
    if records["MX"] and not spf_records:
        results.append(
            finding(
                "Email Security",
                "SPF record not detected",
                "Medium",
                "The domain receives email but no SPF policy was identified.",
                host,
                "Publish and maintain an SPF policy for authorised mail senders.",
                url,
                confidence="High",
                cwe="CWE-290",
            )
        )
    if records["MX"] and not records["DMARC"]:
        results.append(
            finding(
                "Email Security",
                "DMARC record not detected",
                "Medium",
                "The domain receives email but no DMARC policy was identified.",
                f"_dmarc.{host}",
                "Publish a DMARC policy and monitor alignment reports.",
                url,
                confidence="High",
                cwe="CWE-290",
            )
        )
    elif records["DMARC"]:
        policy = " ".join(records["DMARC"]).lower()
        if "p=none" in policy:
            results.append(
                finding(
                    "Email Security",
                    "DMARC policy is monitoring only",
                    "Low",
                    "The DMARC policy does not request quarantine or rejection.",
                    policy,
                    "After monitoring and alignment validation, consider a stronger DMARC policy.",
                    url,
                    confidence="High",
                )
            )

    return results, records, elapsed_ms
