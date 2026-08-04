from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Comment

from app.models import Finding
from app.scanners.common import finding


LIBRARY_PATTERNS = {
    "jQuery": re.compile(r"jquery(?:-|\.)(\d+(?:\.\d+){1,2})", re.IGNORECASE),
    "Bootstrap": re.compile(r"bootstrap(?:\.min)?(?:-|\.)(\d+(?:\.\d+){1,2})", re.IGNORECASE),
    "AngularJS": re.compile(r"angular(?:\.min)?(?:-|\.)(\d+(?:\.\d+){1,2})", re.IGNORECASE),
}


def scan_content(url: str, document: str) -> tuple[list[Finding], dict[str, object]]:
    results: list[Finding] = []
    soup = BeautifulSoup(document, "html.parser")
    parsed = urlparse(url)
    mixed_resources: list[str] = []
    external_domains: set[str] = set()
    inline_scripts = 0

    for tag, attribute in (("script", "src"), ("img", "src"), ("link", "href"), ("iframe", "src")):
        for node in soup.find_all(tag):
            value = (node.get(attribute) or "").strip()
            if not value:
                if tag == "script" and node.string:
                    inline_scripts += 1
                continue
            absolute = urljoin(url, value)
            resource = urlparse(absolute)
            if parsed.scheme == "https" and resource.scheme == "http":
                mixed_resources.append(absolute)
            if resource.hostname and resource.hostname != parsed.hostname:
                external_domains.add(resource.hostname)

    if mixed_resources:
        results.append(
            finding(
                "Transport Security",
                "Mixed content resources detected",
                "High",
                "The HTTPS page references resources over unencrypted HTTP.",
                "\n".join(mixed_resources[:20]),
                "Load all page resources through HTTPS.",
                url,
                cwe="CWE-319",
            )
        )

    comments = [str(item).strip() for item in soup.find_all(string=lambda text: isinstance(text, Comment))]
    sensitive_comments = [
        comment for comment in comments if any(token in comment.lower() for token in ("todo", "password", "secret", "api key", "internal", "debug"))
    ]
    if sensitive_comments:
        results.append(
            finding(
                "Information Disclosure",
                "Potentially sensitive HTML comments",
                "Low",
                "Source comments contain terms that may reveal implementation details.",
                "\n".join(sensitive_comments[:10]),
                "Remove internal notes and sensitive implementation details from production HTML.",
                url,
                confidence="Medium",
                cwe="CWE-200",
            )
        )

    generator = soup.find("meta", attrs={"name": re.compile("^generator$", re.IGNORECASE)})
    if generator and generator.get("content"):
        results.append(
            finding(
                "Technology",
                "Generator metadata disclosed",
                "Low",
                "The page exposes generator or content management system information.",
                str(generator.get("content")),
                "Remove generator metadata when it is not operationally required.",
                url,
                cwe="CWE-200",
            )
        )

    detected_libraries: dict[str, str] = {}
    for script in soup.find_all("script", src=True):
        source = str(script.get("src"))
        for name, pattern in LIBRARY_PATTERNS.items():
            match = pattern.search(source)
            if match:
                detected_libraries[name] = match.group(1)

    metadata = {
        "title": soup.title.string.strip() if soup.title and soup.title.string else "",
        "forms": len(soup.find_all("form")),
        "scripts": len(soup.find_all("script")),
        "inline_scripts": inline_scripts,
        "external_domains": sorted(external_domains),
        "detected_libraries": detected_libraries,
        "html_comments": len(comments),
    }
    return results, metadata
