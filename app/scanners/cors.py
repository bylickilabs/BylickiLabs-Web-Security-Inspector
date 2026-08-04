from __future__ import annotations

from app.models import Finding
from app.scanners.common import finding


def scan_cors(url: str, headers: dict[str, str], probe_origin: str = "") -> list[Finding]:
    results: list[Finding] = []
    normalized = {key.lower(): value for key, value in headers.items()}
    origin = normalized.get("access-control-allow-origin", "")
    credentials = normalized.get("access-control-allow-credentials", "").lower()

    if origin == "*" and credentials == "true":
        results.append(
            finding(
                "CORS",
                "Wildcard origin combined with credentials",
                "High",
                "The response combines a wildcard origin with credential support.",
                "Access-Control-Allow-Origin: *; Access-Control-Allow-Credentials: true",
                "Use an explicit allowlist and review credential requirements.",
                url,
                cwe="CWE-942",
            )
        )
    elif origin == "*":
        results.append(
            finding(
                "CORS",
                "Wildcard cross origin access",
                "Low",
                "The resource permits requests from any origin.",
                "Access-Control-Allow-Origin: *",
                "Confirm that the resource is intentionally public and does not expose sensitive data.",
                url,
                confidence="Medium",
                cwe="CWE-942",
            )
        )

    if probe_origin and origin == probe_origin:
        results.append(
            finding(
                "CORS",
                "Arbitrary origin appears to be reflected",
                "High" if credentials == "true" else "Medium",
                "The server reflected the supplied cross origin value.",
                f"Reflected origin: {origin}; credentials: {credentials or 'not declared'}",
                "Validate origins against a strict allowlist and never reflect untrusted values.",
                url,
                cwe="CWE-942",
            )
        )
    if origin == "null":
        results.append(
            finding(
                "CORS",
                "Null origin is permitted",
                "Medium",
                "The server permits the special null origin.",
                "Access-Control-Allow-Origin: null",
                "Remove null origin access unless it is explicitly required and risk assessed.",
                url,
                cwe="CWE-942",
            )
        )
    return results
