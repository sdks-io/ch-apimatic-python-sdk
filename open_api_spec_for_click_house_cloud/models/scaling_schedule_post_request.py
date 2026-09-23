from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scaling_schedule_entry_request import ScalingScheduleEntryRequest, ScalingScheduleEntryRequestDict


class ScalingSchedulePostRequest(SdkBaseModel):
    entries: list[ScalingScheduleEntryRequest]
    """List of schedule entries. Pass an empty array to clear the schedule."""


class ScalingSchedulePostRequestDict(TypedDict):
    entries: list[ScalingScheduleEntryRequestDict]
