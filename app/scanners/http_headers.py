from __future__ import annotations

from app.models import Finding
from app.scanners.common import finding


RECOMMENDED_HEADERS: dict[str, tuple[str, str, str]] = {
    "strict-transport-security": (
        "High",
        "HTTP Strict Transport Security is not configured.",
        "Enable HSTS with an appropriate max age after validating HTTPS coverage.",
    ),
    "content-security-policy": (
        "High",
        "No Content Security Policy was detected.",
        "Deploy a restrictive Content Security Policy and avoid unsafe directives.",
    ),
    "x-content-type-options": (
        "Medium",
        "MIME type sniffing is not explicitly disabled.",
        "Set X Content Type Options to nosniff.",
    ),
    "referrer-policy": (
        "Low",
        "No explicit referrer policy was detected.",
        "Configure an appropriate Referrer Policy such as strict origin when cross origin.",
    ),
    "permissions-policy": (
        "Low",
        "Browser feature permissions are not explicitly restricted.",
        "Define a Permissions Policy for unnecessary browser capabilities.",
    ),
    "cross-origin-opener-policy": (
        "Low",
        "Cross origin opener isolation is not configured.",
        "Evaluate Cross Origin Opener Policy for sensitive applications.",
    ),
    "cross-origin-resource-policy": (
        "Low",
        "Cross origin resource policy is not configured.",
        "Restrict cross origin resource loading where appropriate.",
    ),
}


def scan_headers(url: str, headers: dict[str, str], is_https: bool) -> list[Finding]:
    results: list[Finding] = []
    normalized = {key.lower(): value for key, value in headers.items()}

    for name, (severity, description, remediation) in RECOMMENDED_HEADERS.items():
        if name == "strict-transport-security" and not is_https:
            continue
        if name not in normalized:
            results.append(
                finding(
                    "HTTP Headers",
                    f"Missing {name}",
                    severity,
                    description,
                    f"Header not present: {name}",
                    remediation,
                    url,
                    cwe="CWE-693",
                )
            )

    csp = normalized.get("content-security-policy", "")
    if csp:
        weak_tokens = [token for token in ("'unsafe-inline'", "'unsafe-eval'", "*") if token in csp]
        if weak_tokens:
            results.append(
                finding(
                    "Content Security Policy",
                    "Potentially permissive CSP directives",
                    "Medium",
                    "The Content Security Policy contains directives that can weaken script isolation.",
                    ", ".join(weak_tokens),
                    "Reduce permissive sources and use nonces or hashes for scripts where possible.",
                    url,
                    confidence="Medium",
                    cwe="CWE-693",
                )
            )
        if "object-src" not in csp:
            results.append(
                finding(
                    "Content Security Policy",
                    "CSP does not define object src",
                    "Low",
                    "The policy does not explicitly restrict plugin based content.",
                    csp,
                    "Add object src 'none' unless object content is required.",
                    url,
                    confidence="Medium",
                )
            )

    hsts = normalized.get("strict-transport-security", "")
    if hsts:
        lower = hsts.lower()
        if "max-age=" not in lower:
            results.append(
                finding(
                    "HTTP Headers",
                    "Invalid HSTS configuration",
                    "Medium",
                    "The HSTS header does not contain a max age directive.",
                    hsts,
                    "Define a valid max age value.",
                    url,
                )
            )
        elif "max-age=0" in lower:
            results.append(
                finding(
                    "HTTP Headers",
                    "HSTS is effectively disabled",
                    "High",
                    "The HSTS policy uses a max age of zero.",
                    hsts,
                    "Set an appropriate nonzero max age after confirming HTTPS readiness.",
                    url,
                )
            )

    xfo = normalized.get("x-frame-options", "")
    if not xfo and "frame-ancestors" not in csp:
        results.append(
            finding(
                "HTTP Headers",
                "Missing frame embedding protection",
                "Medium",
                "Neither X Frame Options nor CSP frame ancestors was detected.",
                "No frame protection header found",
                "Configure CSP frame ancestors or X Frame Options.",
                url,
                cwe="CWE-1021",
            )
        )

    server = normalized.get("server")
    powered_by = normalized.get("x-powered-by")
    if server:
        results.append(
            finding(
                "Information Disclosure",
                "Server information disclosed",
                "Low",
                "The server response reveals platform information.",
                server,
                "Minimise unnecessary server and version disclosure.",
                url,
                confidence="High",
                cwe="CWE-200",
            )
        )
    if powered_by:
        results.append(
            finding(
                "Information Disclosure",
                "Technology header disclosed",
                "Low",
                "The X Powered By header reveals implementation details.",
                powered_by,
                "Remove unnecessary technology disclosure headers.",
                url,
                cwe="CWE-200",
            )
        )

    cache_control = normalized.get("cache-control", "").lower()
    pragma = normalized.get("pragma", "").lower()
    if any(token in url.lower() for token in ("login", "account", "admin", "profile")):
        if "no-store" not in cache_control and "no-cache" not in pragma:
            results.append(
                finding(
                    "Caching",
                    "Sensitive page may be cacheable",
                    "Medium",
                    "The URL appears sensitive but restrictive cache controls were not detected.",
                    f"Cache-Control: {cache_control or '(missing)'}",
                    "Use no store for responses containing sensitive information.",
                    url,
                    confidence="Medium",
                    cwe="CWE-525",
                )
            )

    return results
