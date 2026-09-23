from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.start_hour_utc1 import StartHourUtc1OrInt


class UpgradeWindowPutRequest(SdkBaseModel):
    weekday: int
    """Day of the week the upgrade window starts. 0 = Sunday, 1 = Monday, …, 6 = Saturday."""

    start_hour_utc: StartHourUtc1OrInt = Field(alias="startHourUtc")
    """UTC hour when the upgrade window starts. Must be one of 0, 6, 12, or 18. The upgrade window currently lasts 6
    hours from this start time."""


class UpgradeWindowPutRequestDict(TypedDict):
    weekday: int
    start_hour_utc: StartHourUtc1OrInt
