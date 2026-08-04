from __future__ import annotations

from urllib.parse import urljoin, urlparse

import requests

from app.config import MAX_RESPONSE_BYTES, USER_AGENT
from app.models import Finding
from app.scanners.common import finding


RESOURCE_CHECKS: tuple[tuple[str, str, str], ...] = (
    ("/.well-known/security.txt", "Security contact file", "Info"),
    ("/security.txt", "Security contact file", "Info"),
    ("/robots.txt", "Robots instructions", "Info"),
    ("/sitemap.xml", "XML sitemap", "Info"),
    ("/.git/HEAD", "Exposed Git metadata", "Critical"),
    ("/.env", "Exposed environment file", "Critical"),
    ("/backup.zip", "Public backup archive", "High"),
    ("/database.sql", "Public database export", "Critical"),
    ("/phpinfo.php", "Public PHP information page", "High"),
    ("/server-status", "Public server status page", "High"),
)


def _same_origin_url(base_url: str, path: str) -> str:
    parsed = urlparse(base_url)
    origin = f"{parsed.scheme}://{parsed.netloc}/"
    return urljoin(origin, path.lstrip("/"))


def scan_resources(base_url: str, session: requests.Session, timeout: int, verify_tls: bool) -> tuple[list[Finding], dict[str, int]]:
    results: list[Finding] = []
    statuses: dict[str, int] = {}
    for path, label, severity in RESOURCE_CHECKS:
        target = _same_origin_url(base_url, path)
        try:
            response = session.get(
                target,
                headers={"User-Agent": USER_AGENT, "Range": f"bytes=0-{MAX_RESPONSE_BYTES - 1}"},
                timeout=timeout,
                verify=verify_tls,
                allow_redirects=False,
                stream=True,
            )
            statuses[path] = response.status_code
            content = response.raw.read(1024, decode_content=True)
            preview = content.decode("utf-8", errors="replace")[:500]
            content_type = response.headers.get("Content-Type", "")
            if path in {"/.git/HEAD", "/.env", "/backup.zip", "/database.sql", "/phpinfo.php", "/server-status"} and response.status_code == 200:
                false_positive = "text/html" in content_type.lower() and any(
                    marker in preview.lower() for marker in ("not found", "404", "page not found")
                )
                if not false_positive:
                    results.append(
                        finding(
                            "Public Resources",
                            label,
                            severity,
                            "A potentially sensitive resource is publicly reachable.",
                            f"URL: {target}\nStatus: {response.status_code}\nContent-Type: {content_type}\nPreview: {preview}",
                            "Remove public access, rotate affected secrets and review deployment artefacts.",
                            target,
                            confidence="High" if path in {"/.git/HEAD", "/.env"} else "Medium",
                            cwe="CWE-200",
                        )
                    )
            elif path.endswith("security.txt") and response.status_code != 200:
                results.append(
                    finding(
                        "Security Contact",
                        "No reachable security.txt file",
                        "Info",
                        "A standard security contact file was not found at this path.",
                        f"{target}: HTTP {response.status_code}",
                        "Publish a current security.txt file under the well known path where appropriate.",
                        target,
                        confidence="High",
                    )
                )
        except requests.RequestException:
            statuses[path] = 0
    return results, statuses
