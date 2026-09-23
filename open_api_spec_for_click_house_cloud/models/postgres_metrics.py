from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .postgres_metric import PostgresMetric, PostgresMetricDict


class PostgresMetrics(SdkBaseModel):
    metrics: list[PostgresMetric]
    """Available metrics, each with its bucketed time series."""


class PostgresMetricsDict(TypedDict):
    metrics: list[PostgresMetricDict]
