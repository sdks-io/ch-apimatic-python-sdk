from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.start_hour_utc import StartHourUtcOrInt


class UpgradeWindow(SdkBaseModel):
    weekday: int
    """Day of the week the upgrade window starts. 0 = Sunday, 1 = Monday, …, 6 = Saturday."""

    start_hour_utc: StartHourUtcOrInt = Field(alias="startHourUtc")
    """UTC hour when the upgrade window starts. Must be one of 0, 6, 12, or 18."""

    duration: Literal[6] = 6
    """Length of the upgrade window in hours. Currently only a 6-hour window is supported."""


class UpgradeWindowDict(TypedDict):
    weekday: int
    start_hour_utc: StartHourUtcOrInt
    duration: Literal[6]
