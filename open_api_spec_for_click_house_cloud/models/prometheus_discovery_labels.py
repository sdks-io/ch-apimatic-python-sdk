from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrometheusDiscoveryLabels(SdkBaseModel):
    scheme: Optional[str] = Field(default=UNSET, alias="__scheme__")
    """URL scheme Prometheus must scrape the target with."""

    metrics_path: Optional[str] = Field(default=UNSET, alias="__metrics_path__")
    """Path of the per-service Prometheus metrics endpoint."""

    param_filtered_metrics: Optional[str] = Field(default=UNSET, alias="__param_filtered_metrics")
    """Value passed as the filtered_metrics query parameter on each scrape."""

    clickhouse_org_id: Optional[UUID] = UNSET
    """Organization ID the service belongs to."""

    clickhouse_service_id: Optional[UUID] = UNSET
    """Service ID."""

    clickhouse_discovery_service_name: Optional[str] = UNSET
    """Service name."""


class PrometheusDiscoveryLabelsDict(TypedDict):
    scheme: NotRequired[str]
    metrics_path: NotRequired[str]
    param_filtered_metrics: NotRequired[str]
    clickhouse_org_id: NotRequired[UUID]
    clickhouse_service_id: NotRequired[UUID]
    clickhouse_discovery_service_name: NotRequired[str]
