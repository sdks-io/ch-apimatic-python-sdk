from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .postgres_metric_series import PostgresMetricSeries, PostgresMetricSeriesDict


class PostgresMetric(SdkBaseModel):
    key: str
    """Stable metric identifier (for example cpu_usage, connection_count, cache_hit_ratio)."""

    name: str
    """Human-readable metric name."""

    unit: str
    """Unit of the metric values (for example %, IOPS, bytes/s, count)."""

    description: str
    """Human-readable description of what the metric measures."""

    series: list[PostgresMetricSeries]
    """One series per label dimension of the metric."""


class PostgresMetricDict(TypedDict):
    key: str
    name: str
    unit: str
    description: str
    series: list[PostgresMetricSeriesDict]
