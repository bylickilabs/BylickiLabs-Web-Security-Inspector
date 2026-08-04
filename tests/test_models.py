from app.models import Finding, ScanMetrics, ScanResult


def make_result() -> ScanResult:
    return ScanResult(
        target="https://example.com/",
        profile="Standard",
        findings=[
            Finding("HTTP Headers", "Missing CSP", "High", "High", "d", "e", "r", "https://example.com/"),
            Finding("Cookies", "Cookie", "Medium", "Medium", "d", "e", "r", "https://example.com/"),
            Finding("DNS", "CAA", "Low", "High", "d", "e", "r", "https://example.com/"),
        ],
        metrics=ScanMetrics(response_samples_ms=[100.0, 120.0, 110.0]),
        started_at="2026-08-02T08:00:00+00:00",
        completed_at="2026-08-02T08:00:02+00:00",
        duration_seconds=2.0,
        application_version="2.0.0",
    )


def test_scan_result_score_and_grade() -> None:
    result = make_result()
    assert result.risk_score > 0
    assert result.grade in {"A", "B", "C", "D", "E"}
    assert result.severity_counts["High"] == 1
    assert result.severity_counts["Critical"] == 0


def test_serialisation_round_trip() -> None:
    result = make_result()
    restored = ScanResult.from_dict(result.to_dict())
    assert restored.target == result.target
    assert restored.findings[0].title == "Missing CSP"
    assert restored.metrics.response_samples_ms == [100.0, 120.0, 110.0]
