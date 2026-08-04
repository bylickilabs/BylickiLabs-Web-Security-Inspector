from __future__ import annotations

import socket
import ssl
import time
from datetime import datetime, timezone
from typing import Any

from app.models import Finding
from app.scanners.common import finding


def scan_tls(host: str, port: int, url: str, timeout: int) -> tuple[list[Finding], dict[str, Any], float]:
    results: list[Finding] = []
    metadata: dict[str, Any] = {}
    start = time.perf_counter()
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, port), timeout=timeout) as raw_socket:
            with context.wrap_socket(raw_socket, server_hostname=host) as secure_socket:
                certificate = secure_socket.getpeercert()
                cipher = secure_socket.cipher()
                metadata = {
                    "protocol": secure_socket.version() or "",
                    "cipher": cipher[0] if cipher else "",
                    "cipher_bits": cipher[2] if cipher else 0,
                    "subject": certificate.get("subject", []),
                    "issuer": certificate.get("issuer", []),
                    "serial_number": certificate.get("serialNumber", ""),
                    "subject_alt_names": certificate.get("subjectAltName", []),
                    "not_before": certificate.get("notBefore", ""),
                    "not_after": certificate.get("notAfter", ""),
                }
        elapsed_ms = (time.perf_counter() - start) * 1000
    except (OSError, ssl.SSLError) as exc:
        elapsed_ms = (time.perf_counter() - start) * 1000
        results.append(
            finding(
                "TLS",
                "TLS connection failed",
                "High",
                "A validated TLS connection could not be established.",
                str(exc),
                "Review certificate validity, hostname coverage and TLS configuration.",
                url,
                cwe="CWE-295",
            )
        )
        return results, metadata, elapsed_ms

    expiry_text = metadata.get("not_after", "")
    if expiry_text:
        try:
            expiry = datetime.strptime(expiry_text, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
            days_remaining = (expiry - datetime.now(timezone.utc)).days
            metadata["days_remaining"] = days_remaining
            if days_remaining < 0:
                severity = "Critical"
                title = "TLS certificate has expired"
            elif days_remaining < 14:
                severity = "High"
                title = "TLS certificate expires very soon"
            elif days_remaining < 30:
                severity = "Medium"
                title = "TLS certificate expires soon"
            else:
                severity = "Info"
                title = "TLS certificate validity"
            if severity != "Info":
                results.append(
                    finding(
                        "TLS",
                        title,
                        severity,
                        "The certificate validity period requires attention.",
                        f"Expiry: {expiry_text}; days remaining: {days_remaining}",
                        "Renew and deploy the certificate before expiration.",
                        url,
                        cwe="CWE-298",
                    )
                )
        except ValueError:
            pass

    protocol = str(metadata.get("protocol", ""))
    if protocol in {"TLSv1", "TLSv1.1"}:
        results.append(
            finding(
                "TLS",
                "Legacy TLS protocol negotiated",
                "High",
                "The connection negotiated a deprecated TLS version.",
                protocol,
                "Disable legacy TLS versions and require TLS 1.2 or newer.",
                url,
                cwe="CWE-326",
            )
        )
    return results, metadata, elapsed_ms
