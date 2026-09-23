from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BackupConfiguration(SdkBaseModel):
    backup_period_in_hours: Optional[float] = Field(default=UNSET, alias="backupPeriodInHours")
    """The interval in hours between each backup."""

    backup_retention_period_in_hours: Optional[float] = Field(default=UNSET, alias="backupRetentionPeriodInHours")
    """The minimum duration in hours for which the backups are available. Must be a whole number of days between 24 (1
    day) and 1080 (45 days) — i.e. a multiple of 24."""

    backup_start_time: Optional[str] = Field(default=UNSET, alias="backupStartTime")
    """The time in HH:MM format for the backups to be performed (evaluated in UTC timezone). When defined the backup
    period resets to every 24 hours."""


class BackupConfigurationDict(TypedDict):
    backup_period_in_hours: NotRequired[float]
    backup_retention_period_in_hours: NotRequired[float]
    backup_start_time: NotRequired[str]
