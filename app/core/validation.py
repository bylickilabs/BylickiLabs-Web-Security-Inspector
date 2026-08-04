from __future__ import annotations

import ipaddress
from urllib.parse import urlparse, urlunparse


def normalize_url(value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError("A target URL is required.")
    if "://" not in value:
        value = f"https://{value}"
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("Only HTTP and HTTPS targets are supported.")
    if not parsed.hostname:
        raise ValueError("The target URL does not contain a valid hostname.")
    netloc = parsed.netloc
    path = parsed.path or "/"
    return urlunparse((parsed.scheme, netloc, path, "", parsed.query, ""))


def is_public_or_local_hostname(hostname: str) -> bool:
    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return bool(hostname and "." in hostname) or hostname == "localhost"
