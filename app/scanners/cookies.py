from __future__ import annotations

from collections.abc import Iterable

from app.models import Finding
from app.scanners.common import finding


def scan_cookies(url: str, set_cookie_headers: Iterable[str]) -> list[Finding]:
    results: list[Finding] = []
    for raw_header in set_cookie_headers:
        if not raw_header:
            continue
        cookie_name = raw_header.split("=", 1)[0].strip() or "unnamed"
        lowered = raw_header.lower()
        if "secure" not in lowered:
            results.append(
                finding(
                    "Cookies",
                    f"Cookie without Secure: {cookie_name}",
                    "Medium",
                    "The cookie is not restricted to encrypted transport.",
                    raw_header,
                    "Add the Secure attribute to cookies transmitted over HTTPS.",
                    url,
                    cwe="CWE-614",
                )
            )
        if "httponly" not in lowered:
            results.append(
                finding(
                    "Cookies",
                    f"Cookie without HttpOnly: {cookie_name}",
                    "Medium",
                    "Client side scripts may be able to access the cookie.",
                    raw_header,
                    "Add HttpOnly where browser scripts do not require cookie access.",
                    url,
                    confidence="Medium",
                    cwe="CWE-1004",
                )
            )
        if "samesite" not in lowered:
            results.append(
                finding(
                    "Cookies",
                    f"Cookie without SameSite: {cookie_name}",
                    "Low",
                    "The cookie does not explicitly define cross site request behaviour.",
                    raw_header,
                    "Set SameSite to Lax or Strict where compatible with application requirements.",
                    url,
                    confidence="Medium",
                    cwe="CWE-1275",
                )
            )
        if "samesite=none" in lowered and "secure" not in lowered:
            results.append(
                finding(
                    "Cookies",
                    f"SameSite None cookie without Secure: {cookie_name}",
                    "High",
                    "A cross site cookie is not restricted to encrypted transport.",
                    raw_header,
                    "Combine SameSite None with the Secure attribute.",
                    url,
                    cwe="CWE-614",
                )
            )
    return results
