from __future__ import annotations

from typing import Any

import requests

from app.models import Finding
from app.scanners.common import finding


def run_pagespeed(url: str, api_key: str, timeout: int) -> tuple[list[Finding], dict[str, float]]:
    endpoint = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed"
    params: list[tuple[str, str]] = [
        ("url", url),
        ("strategy", "desktop"),
        ("category", "performance"),
        ("category", "accessibility"),
        ("category", "best-practices"),
        ("category", "seo"),
    ]
    if api_key:
        params.append(("key", api_key))
    try:
        response = requests.get(endpoint, params=params, timeout=max(timeout, 30))
        response.raise_for_status()
        payload: dict[str, Any] = response.json()
        categories = payload.get("lighthouseResult", {}).get("categories", {})
        scores = {
            name: round(float(value.get("score", 0.0)) * 100, 1)
            for name, value in categories.items()
            if value.get("score") is not None
        }
        results: list[Finding] = []
        for name, score in scores.items():
            if score < 50:
                severity = "Medium"
            elif score < 80:
                severity = "Low"
            else:
                severity = "Info"
            results.append(
                finding(
                    "PageSpeed",
                    f"PageSpeed {name}: {score:.0f}",
                    severity,
                    "Google PageSpeed Insights returned a Lighthouse category score.",
                    f"Category: {name}; Score: {score:.1f}/100",
                    "Review the PageSpeed diagnostics and prioritise high impact recommendations.",
                    url,
                    confidence="High",
                    source="Google PageSpeed Insights",
                )
            )
        return results, scores
    except (requests.RequestException, ValueError, TypeError) as exc:
        return [
            finding(
                "External Services",
                "PageSpeed Insights unavailable",
                "Info",
                "The external PageSpeed service did not return a usable result.",
                str(exc),
                "Retry later or review the configured API key and network access.",
                url,
                confidence="Medium",
                source="Google PageSpeed Insights",
            )
        ], {}


def run_observatory(url: str, timeout: int) -> list[Finding]:
    endpoint = "https://observatory-api.mdn.mozilla.net/api/v2/scan"
    try:
        from urllib.parse import urlparse
        host = urlparse(url).hostname or url
        response = requests.post(endpoint, params={"host": host}, timeout=max(timeout, 30))
        response.raise_for_status()
        payload = response.json()
        grade = payload.get("grade") or payload.get("scan", {}).get("grade") or "Unknown"
        score = payload.get("score") or payload.get("scan", {}).get("score") or "Unknown"
        severity = "Info" if str(grade).upper() in {"A", "A+", "B"} else "Low"
        return [
            finding(
                "External Services",
                f"MDN HTTP Observatory grade: {grade}",
                severity,
                "MDN HTTP Observatory completed an independent HTTP security configuration assessment.",
                f"Grade: {grade}; Score: {score}",
                "Review the detailed Observatory recommendations for the target.",
                url,
                confidence="High",
                source="MDN HTTP Observatory",
            )
        ]
    except (requests.RequestException, ValueError, TypeError) as exc:
        return [
            finding(
                "External Services",
                "MDN HTTP Observatory unavailable",
                "Info",
                "The external Observatory service did not return a usable result.",
                str(exc),
                "Retry later and verify external service availability.",
                url,
                confidence="Medium",
                source="MDN HTTP Observatory",
            )
        ]
