from __future__ import annotations

from app.models import Finding


def finding(
    category: str,
    title: str,
    severity: str,
    description: str,
    evidence: str,
    remediation: str,
    url: str,
    *,
    confidence: str = "High",
    source: str = "Local",
    cwe: str = "",
    reference: str = "",
) -> Finding:
    return Finding(
        category=category,
        title=title,
        severity=severity,
        confidence=confidence,
        description=description,
        evidence=evidence[:4000],
        remediation=remediation,
        url=url,
        source=source,
        cwe=cwe,
        reference=reference,
    )
