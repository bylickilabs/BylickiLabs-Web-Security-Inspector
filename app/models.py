from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from math import exp
from typing import Any
from uuid import uuid4

from app.config import SEVERITY_WEIGHTS


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class Finding:
    category: str
    title: str
    severity: str
    confidence: str
    description: str
    evidence: str
    remediation: str
    url: str
    source: str = "Local"
    cwe: str = ""
    reference: str = ""
    created_at: str = field(default_factory=utc_now)

    @property
    def numeric_weight(self) -> float:
        return SEVERITY_WEIGHTS.get(self.severity, 0.0)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Finding":
        allowed = {field_name for field_name in cls.__dataclass_fields__}
        return cls(**{key: value for key, value in data.items() if key in allowed})


@dataclass(slots=True)
class ScanMetrics:
    status_code: int = 0
    final_url: str = ""
    response_size_bytes: int = 0
    redirect_count: int = 0
    dns_time_ms: float = 0.0
    tls_time_ms: float = 0.0
    response_time_ms: float = 0.0
    response_samples_ms: list[float] = field(default_factory=list)
    checks_executed: int = 0
    pagespeed_scores: dict[str, float] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ScanMetrics":
        return cls(**data)


@dataclass(slots=True)
class ScanResult:
    target: str
    profile: str
    findings: list[Finding]
    metrics: ScanMetrics
    started_at: str
    completed_at: str
    duration_seconds: float
    scan_id: str = field(default_factory=lambda: str(uuid4()))
    application_version: str = ""

    @property
    def severity_counts(self) -> dict[str, int]:
        counts = {name: 0 for name in ("Critical", "High", "Medium", "Low", "Info")}
        for finding in self.findings:
            counts[finding.severity] = counts.get(finding.severity, 0) + 1
        return counts

    @property
    def risk_score(self) -> float:
        confidence_multiplier = {"High": 1.0, "Medium": 0.8, "Low": 0.6}
        adjusted = sum(
            finding.numeric_weight * confidence_multiplier.get(finding.confidence, 0.7)
            for finding in self.findings
        )
        score = 100.0 * (1.0 - exp(-adjusted / 45.0))
        critical_count = self.severity_counts.get("Critical", 0)
        if critical_count:
            score = max(score, min(90.0, 45.0 + critical_count * 10.0))
        return round(min(100.0, score), 1)

    @property
    def grade(self) -> str:
        score = self.risk_score
        if score < 10:
            return "A"
        if score < 25:
            return "B"
        if score < 45:
            return "C"
        if score < 70:
            return "D"
        return "E"

    def to_dict(self) -> dict[str, Any]:
        return {
            "scan_id": self.scan_id,
            "target": self.target,
            "profile": self.profile,
            "findings": [finding.to_dict() for finding in self.findings],
            "metrics": self.metrics.to_dict(),
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "duration_seconds": self.duration_seconds,
            "application_version": self.application_version,
            "risk_score": self.risk_score,
            "grade": self.grade,
            "severity_counts": self.severity_counts,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ScanResult":
        return cls(
            scan_id=data.get("scan_id", str(uuid4())),
            target=data["target"],
            profile=data.get("profile", "Standard"),
            findings=[Finding.from_dict(item) for item in data.get("findings", [])],
            metrics=ScanMetrics.from_dict(data.get("metrics", {})),
            started_at=data.get("started_at", utc_now()),
            completed_at=data.get("completed_at", utc_now()),
            duration_seconds=float(data.get("duration_seconds", 0.0)),
            application_version=data.get("application_version", ""),
        )