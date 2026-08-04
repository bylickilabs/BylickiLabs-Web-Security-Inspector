from app.core.statistics import calculate_statistics, category_series, severity_series
from tests.test_models import make_result


def test_statistics_are_calculated() -> None:
    result = make_result()
    summary = calculate_statistics(result)
    assert summary.finding_count == 3
    assert summary.mean_weight > 0
    assert summary.mean_response_ms == 110.0
    assert summary.percentile_95 >= summary.median_weight


def test_chart_series() -> None:
    result = make_result()
    labels, values = severity_series(result)
    assert labels[0] == "Critical"
    assert sum(values) == 3
    categories, counts = category_series(result)
    assert "HTTP Headers" in categories
    assert sum(counts) == 3
