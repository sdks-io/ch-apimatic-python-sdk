from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .postgres_metric_data_point import PostgresMetricDataPoint, PostgresMetricDataPointDict


class PostgresMetricSeries(SdkBaseModel):
    label: str
    """Distinguishing label for this series within the metric (for example a CPU mode, a database name, or "Reads")."""

    data_points: list[PostgresMetricDataPoint] = Field(alias="dataPoints")
    """Time-ordered data points, one per bucket."""


class PostgresMetricSeriesDict(TypedDict):
    label: str
    data_points: list[PostgresMetricDataPointDict]
