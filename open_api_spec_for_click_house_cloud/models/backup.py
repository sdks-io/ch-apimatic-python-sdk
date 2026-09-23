from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status1 import Status1OrStr
from .enums.type13 import Type13OrStr
from .unions.bucket import Bucket, BucketDict


class Backup(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique backup ID."""

    status: Optional[Status1OrStr] = UNSET
    """Status of the backup: 'done', 'error', 'in_progress'."""

    service_id: Optional[str] = Field(default=UNSET, alias="serviceId")
    """Name"""

    started_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startedAt")
    """Backup start timestamp. ISO-8601."""

    finished_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="finishedAt")
    """Backup finish timestamp. ISO-8601. Available only for finished backups"""

    size_in_bytes: Optional[float] = Field(default=UNSET, alias="sizeInBytes")
    """Size of the backup in bytes."""

    duration_in_seconds: Optional[float] = Field(default=UNSET, alias="durationInSeconds")
    """Time in seconds it took to perform the backup. If the status still in_progress, this is the time in seconds since
    the backup started until now."""

    type_: Optional[Type13OrStr] = Field(default=UNSET, alias="type")
    """Backup type ("full" or "incremental")."""

    backup_name: Optional[str] = Field(default=UNSET, alias="backupName")
    """Backup name on the external backup bucket."""

    bucket: Optional[Bucket] = UNSET
    """Backup bucket where the backup is stored."""


class BackupDict(TypedDict):
    id: NotRequired[UUID]
    status: NotRequired[Status1OrStr]
    service_id: NotRequired[str]
    started_at: NotRequired[RFC3339DateTime]
    finished_at: NotRequired[RFC3339DateTime]
    size_in_bytes: NotRequired[float]
    duration_in_seconds: NotRequired[float]
    type_: NotRequired[Type13OrStr]
    backup_name: NotRequired[str]
    bucket: NotRequired[BucketDict]
