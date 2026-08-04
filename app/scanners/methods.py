from __future__ import annotations

import requests

from app.config import USER_AGENT
from app.models import Finding
from app.scanners.common import finding


def scan_methods(
    url: str,
    session: requests.Session,
    timeout: int,
    verify_tls: bool,
) -> tuple[list[Finding], dict[str, object]]:
    results: list[Finding] = []
    metadata: dict[str, object] = {"allowed_methods": []}
    try:
        options = session.options(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=timeout,
            verify=verify_tls,
            allow_redirects=True,
        )
        allow = options.headers.get("Allow", "")
        methods = [item.strip().upper() for item in allow.split(",") if item.strip()]
        metadata["allowed_methods"] = methods
        dangerous = [method for method in methods if method in {"PUT", "DELETE", "TRACE", "CONNECT"}]
        if dangerous:
            results.append(
                finding(
                    "HTTP Methods",
                    "Potentially sensitive HTTP methods advertised",
                    "Medium",
                    "The server advertises methods that require explicit application controls.",
                    ", ".join(dangerous),
                    "Disable unnecessary methods and enforce authentication and authorisation for required methods.",
                    url,
                    confidence="Medium",
                    cwe="CWE-749",
                )
            )
    except requests.RequestException:
        pass

    try:
        trace = session.request(
            "TRACE",
            url,
            headers={"User-Agent": USER_AGENT, "X-BWSI-Trace": "validation"},
            timeout=timeout,
            verify=verify_tls,
            allow_redirects=False,
        )
        metadata["trace_status"] = trace.status_code
        if trace.status_code == 200 and "X-BWSI-Trace".lower() in trace.text.lower():
            results.append(
                finding(
                    "HTTP Methods",
                    "HTTP TRACE appears enabled",
                    "Medium",
                    "The server accepted TRACE and reflected request data.",
                    f"HTTP {trace.status_code}; reflected validation header",
                    "Disable TRACE unless it is explicitly required.",
                    url,
                    cwe="CWE-693",
                )
            )
    except requests.RequestException:
        metadata["trace_status"] = 0
    return results, metadata
