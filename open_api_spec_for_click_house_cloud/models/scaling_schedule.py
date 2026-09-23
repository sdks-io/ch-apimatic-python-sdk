from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scaling_schedule_base_config import ScalingScheduleBaseConfig, ScalingScheduleBaseConfigDict
from .scaling_schedule_entry import ScalingScheduleEntry, ScalingScheduleEntryDict


class ScalingSchedule(SdkBaseModel):
    entries: list[ScalingScheduleEntry]
    """List of schedule entries."""

    base_config: ScalingScheduleBaseConfig = Field(alias="baseConfig")
    active_entry_id: Optional[UUID] = Field(default=UNSET, alias="activeEntryId")
    """ID of the currently-active schedule entry. Absent when no entry is active and the base config is in effect."""


class ScalingScheduleDict(TypedDict):
    entries: list[ScalingScheduleEntryDict]
    base_config: ScalingScheduleBaseConfigDict
    active_entry_id: NotRequired[UUID]
