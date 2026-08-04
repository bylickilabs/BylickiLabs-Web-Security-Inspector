from __future__ import annotations

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from app.models import Finding
from app.scanners.common import finding


def scan_forms(url: str, document: str) -> list[Finding]:
    results: list[Finding] = []
    soup = BeautifulSoup(document, "html.parser")
    page_host = urlparse(url).hostname

    for index, form in enumerate(soup.find_all("form"), start=1):
        action = urljoin(url, form.get("action") or url)
        method = (form.get("method") or "GET").upper()
        action_parsed = urlparse(action)
        password_fields = form.find_all("input", attrs={"type": lambda value: value and value.lower() == "password"})

        if action_parsed.scheme == "http":
            results.append(
                finding(
                    "Forms",
                    f"Form {index} submits over HTTP",
                    "High",
                    "The form submits data to an unencrypted endpoint.",
                    action,
                    "Use HTTPS for all form submissions.",
                    url,
                    cwe="CWE-319",
                )
            )
        if password_fields and method == "GET":
            results.append(
                finding(
                    "Forms",
                    f"Password form {index} uses GET",
                    "High",
                    "Password values may be placed in URLs, logs and browser history.",
                    f"Method: {method}; Action: {action}",
                    "Submit authentication forms using POST over HTTPS.",
                    url,
                    cwe="CWE-598",
                )
            )
        if action_parsed.hostname and action_parsed.hostname != page_host:
            results.append(
                finding(
                    "Forms",
                    f"Form {index} submits to another domain",
                    "Medium",
                    "The form transmits data to a host different from the current page.",
                    action,
                    "Verify the external destination and disclose third party processing where required.",
                    url,
                    confidence="Medium",
                    cwe="CWE-441",
                )
            )

        token_names = ("csrf", "xsrf", "token", "nonce", "authenticity")
        token = form.find("input", attrs={"name": lambda name: bool(name and any(item in name.lower() for item in token_names))})
        if method == "POST" and not token:
            results.append(
                finding(
                    "Forms",
                    f"No visible request token in form {index}",
                    "Low",
                    "No common anti request forgery token field was identified in the HTML form.",
                    f"Method: {method}; Action: {action}",
                    "Confirm that the application uses an effective anti request forgery control.",
                    url,
                    confidence="Low",
                    cwe="CWE-352",
                )
            )

        for field in form.find_all("input"):
            field_type = (field.get("type") or "text").lower()
            if field_type in {"password", "email", "tel"} and not field.has_attr("autocomplete"):
                results.append(
                    finding(
                        "Forms",
                        f"Sensitive field without autocomplete policy in form {index}",
                        "Info",
                        "A sensitive input does not define an explicit browser autocomplete policy.",
                        str(field)[:500],
                        "Set a suitable autocomplete value for authentication and personal data fields.",
                        url,
                        confidence="Medium",
                    )
                )
                break
    return results
