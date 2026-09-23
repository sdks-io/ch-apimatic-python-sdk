from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SnapshotConfiguration(SdkBaseModel):
    enabled: Optional[bool] = UNSET
    """Whether scheduled snapshots are enabled for the service."""

    gap: Optional[float] = UNSET
    """Interval between snapshots, in minutes. Set together with timeFrame; only supported preset pairs are accepted."""

    time_frame: Optional[float] = Field(default=UNSET, alias="timeFrame")
    """Retention window the snapshots cover, in minutes. Set together with gap; only supported preset pairs are
    accepted."""


class SnapshotConfigurationDict(TypedDict):
    enabled: NotRequired[bool]
    gap: NotRequired[float]
    time_frame: NotRequired[float]
