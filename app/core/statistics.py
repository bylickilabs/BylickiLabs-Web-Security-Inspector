from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable

import numpy as np
from scipy import stats

from app.config import SEVERITY_ORDER, SEVERITY_WEIGHTS
from app.models import ScanResult


@dataclass(slots=True)
class StatisticalSummary:
    finding_count: int
    mean_weight: float
    median_weight: float
    standard_deviation: float
    percentile_75: float
    percentile_95: float
    skewness: float
    entropy: float
    mean_response_ms: float
    median_response_ms: float
    response_standard_deviation: float
    trend_slope: float
    outlier_count: int

    def to_dict(self) -> dict[str, float | int]:
        return {name: getattr(self, name) for name in self.__dataclass_fields__}


def _safe_float(value: float) -> float:
    return round(float(value), 3) if np.isfinite(value) else 0.0


def severity_series(result: ScanResult) -> tuple[list[str], list[int]]:
    counts = result.severity_counts
    return SEVERITY_ORDER, [counts.get(name, 0) for name in SEVERITY_ORDER]


def category_series(result: ScanResult) -> tuple[list[str], list[int]]:
    counter = Counter(finding.category for finding in result.findings)
    labels = [name for name, _ in counter.most_common()]
    return labels, [counter[label] for label in labels]


def confidence_series(result: ScanResult) -> tuple[list[str], list[int]]:
    counter = Counter(finding.confidence for finding in result.findings)
    labels = ["High", "Medium", "Low"]
    return labels, [counter.get(label, 0) for label in labels]


def calculate_statistics(result: ScanResult) -> StatisticalSummary:
    weights = np.asarray(
        [SEVERITY_WEIGHTS.get(finding.severity, 0.0) for finding in result.findings],
        dtype=float,
    )
    response = np.asarray(result.metrics.response_samples_ms, dtype=float)

    if weights.size:
        probabilities = np.asarray(list(result.severity_counts.values()), dtype=float)
        probabilities = probabilities[probabilities > 0]
        probabilities = probabilities / probabilities.sum() if probabilities.size else probabilities
        entropy = stats.entropy(probabilities, base=2) if probabilities.size else 0.0
        skewness = stats.skew(weights, bias=False) if weights.size >= 3 else 0.0
        mean_weight = np.mean(weights)
        median_weight = np.median(weights)
        std_weight = np.std(weights, ddof=1) if weights.size > 1 else 0.0
        p75 = np.percentile(weights, 75)
        p95 = np.percentile(weights, 95)
    else:
        mean_weight = median_weight = std_weight = p75 = p95 = skewness = entropy = 0.0

    if response.size:
        mean_response = np.mean(response)
        median_response = np.median(response)
        response_std = np.std(response, ddof=1) if response.size > 1 else 0.0
        if response.size > 1:
            x = np.arange(response.size, dtype=float)
            trend_slope = stats.linregress(x, response).slope
        else:
            trend_slope = 0.0
        if response.size >= 3 and response_std > 0:
            z_scores = np.abs(stats.zscore(response, nan_policy="omit"))
            outlier_count = int(np.sum(z_scores > 2.0))
        else:
            outlier_count = 0
    else:
        mean_response = median_response = response_std = trend_slope = 0.0
        outlier_count = 0

    return StatisticalSummary(
        finding_count=len(result.findings),
        mean_weight=_safe_float(mean_weight),
        median_weight=_safe_float(median_weight),
        standard_deviation=_safe_float(std_weight),
        percentile_75=_safe_float(p75),
        percentile_95=_safe_float(p95),
        skewness=_safe_float(skewness),
        entropy=_safe_float(entropy),
        mean_response_ms=_safe_float(mean_response),
        median_response_ms=_safe_float(median_response),
        response_standard_deviation=_safe_float(response_std),
        trend_slope=_safe_float(trend_slope),
        outlier_count=outlier_count,
    )


def history_trend(results: Iterable[ScanResult]) -> tuple[list[str], list[float]]:
    ordered = sorted(results, key=lambda item: item.completed_at)
    labels = [item.completed_at[:10] for item in ordered]
    return labels, [item.risk_score for item in ordered]
