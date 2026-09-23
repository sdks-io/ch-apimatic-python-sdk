from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PostgresMetricDataPoint(SdkBaseModel):
    timestamp: int
    """Bucket start time as a Unix timestamp in seconds."""

    value: float
    """Metric value for the bucket."""


class PostgresMetricDataPointDict(TypedDict):
    timestamp: int
    value: float
