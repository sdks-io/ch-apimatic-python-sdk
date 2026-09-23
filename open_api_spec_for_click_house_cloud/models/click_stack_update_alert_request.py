from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.interval import IntervalOrStr
from .enums.source import SourceOrStr
from .enums.threshold_type import ThresholdTypeOrStr
from .unions.click_stack_alert_channel import ClickStackAlertChannel, ClickStackAlertChannelDict


class ClickStackUpdateAlertRequest(SdkBaseModel):
    dashboard_id: OptionalNullable[str] = Field(default=UNSET, alias="dashboardId")
    """Dashboard ID for tile-based alerts."""

    tile_id: OptionalNullable[str] = Field(default=UNSET, alias="tileId")
    """Tile ID for tile-based alerts. Must be a line, stacked bar, or number type tile."""

    saved_search_id: OptionalNullable[str] = Field(default=UNSET, alias="savedSearchId")
    """Saved search ID for saved_search alerts."""

    group_by: OptionalNullable[str] = Field(default=UNSET, alias="groupBy")
    """Group-by key for saved search alerts."""

    threshold: Optional[float] = UNSET
    """Threshold value for triggering the alert. For between and not_between threshold types, this is the lower
    bound."""

    threshold_max: OptionalNullable[float] = Field(default=UNSET, alias="thresholdMax")
    """Upper bound for between and not_between threshold types. Required when thresholdType is between or not_between,
    must be >= threshold."""

    interval: Optional[IntervalOrStr] = UNSET
    """Evaluation interval for the alert. ``30s`` requires the 30s alert interval feature to be enabled for your
    team."""

    schedule_offset_minutes: OptionalNullable[int] = Field(default=UNSET, alias="scheduleOffsetMinutes")
    """Offset from the interval boundary in minutes. For example, 2 with a 5m interval evaluates windows at :02, :07,
    :12, etc. (UTC)."""

    schedule_start_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="scheduleStartAt")
    """Absolute UTC start time anchor. Alert windows start from this timestamp and repeat every interval."""

    source: Optional[SourceOrStr] = UNSET
    """Alert source type (tile-based or saved search)."""

    threshold_type: Optional[ThresholdTypeOrStr] = Field(default=UNSET, alias="thresholdType")
    """Threshold comparison direction."""

    channel: Optional[ClickStackAlertChannel] = UNSET
    channels: Optional[list[ClickStackAlertChannel]] = UNSET
    """Notification channels to trigger when the alert fires or resolves. Between 1 and 10 channels; duplicates are
    rejected."""

    name: OptionalNullable[str] = UNSET
    """Human-friendly alert name."""

    message: OptionalNullable[str] = UNSET
    """Alert message template."""

    note: OptionalNullable[str] = UNSET
    """Freeform note for the alert. Supports markdown formatting."""

    num_consecutive_windows: OptionalNullable[int] = Field(default=UNSET, alias="numConsecutiveWindows")
    """Fire the alert only after its condition has been met for this many consecutive evaluation windows. While the
    condition is met but fewer than this many consecutive windows have violated, the alert is in the PENDING state."""


class ClickStackUpdateAlertRequestDict(TypedDict):
    dashboard_id: NotRequired[str | None]
    tile_id: NotRequired[str | None]
    saved_search_id: NotRequired[str | None]
    group_by: NotRequired[str | None]
    threshold: NotRequired[float]
    threshold_max: NotRequired[float | None]
    interval: NotRequired[IntervalOrStr]
    schedule_offset_minutes: NotRequired[int | None]
    schedule_start_at: NotRequired[RFC3339DateTime | None]
    source: NotRequired[SourceOrStr]
    threshold_type: NotRequired[ThresholdTypeOrStr]
    channel: NotRequired[ClickStackAlertChannelDict]
    channels: NotRequired[list[ClickStackAlertChannelDict]]
    name: NotRequired[str | None]
    message: NotRequired[str | None]
    note: NotRequired[str | None]
    num_consecutive_windows: NotRequired[int | None]
