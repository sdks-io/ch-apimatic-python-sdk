from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .prometheus_discovery_labels import PrometheusDiscoveryLabels, PrometheusDiscoveryLabelsDict


class PrometheusDiscoveryTargetGroup(SdkBaseModel):
    targets: Optional[list[str]] = UNSET
    """Host (and port) of the ClickHouse Cloud API."""

    labels: Optional[PrometheusDiscoveryLabels] = UNSET


class PrometheusDiscoveryTargetGroupDict(TypedDict):
    targets: NotRequired[list[str]]
    labels: NotRequired[PrometheusDiscoveryLabelsDict]
