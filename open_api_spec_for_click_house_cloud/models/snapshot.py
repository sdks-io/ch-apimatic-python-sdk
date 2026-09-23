from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status2 import Status2OrStr
from .enums.type14 import Type14OrStr
from .unions.bucket1 import Bucket1, Bucket1Dict


class Snapshot(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique snapshot ID."""

    status: Optional[Status2OrStr] = UNSET
    """Status of the snapshot: 'done', 'error', 'in_progress', 'throttled'. 'throttled' means snapshot creation was
    rate-limited and will be retried."""

    service_id: Optional[str] = Field(default=UNSET, alias="serviceId")
    """ID of the service the snapshot was created from."""

    started_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startedAt")
    """Snapshot start timestamp. ISO-8601."""

    finished_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="finishedAt")
    """Snapshot finish timestamp. ISO-8601. Available only for finished snapshots"""

    size_in_bytes: Optional[float] = Field(default=UNSET, alias="sizeInBytes")
    """Size of the snapshot in bytes."""

    duration_in_seconds: Optional[float] = Field(default=UNSET, alias="durationInSeconds")
    """Time in seconds it took to perform the snapshot. If the status is in_progress or throttled, this is the time in
    seconds since the snapshot started until now."""

    type_: Optional[Type14OrStr] = Field(default=UNSET, alias="type")
    """Snapshot type. Always "full" — snapshots never chain off a parent."""

    backup_name: Optional[str] = Field(default=UNSET, alias="backupName")
    """Snapshot name on the external backup bucket."""

    bucket: Optional[Bucket1] = UNSET
    """Backup bucket where the snapshot is stored."""


class SnapshotDict(TypedDict):
    id: NotRequired[UUID]
    status: NotRequired[Status2OrStr]
    service_id: NotRequired[str]
    started_at: NotRequired[RFC3339DateTime]
    finished_at: NotRequired[RFC3339DateTime]
    size_in_bytes: NotRequired[float]
    duration_in_seconds: NotRequired[float]
    type_: NotRequired[Type14OrStr]
    backup_name: NotRequired[str]
    bucket: NotRequired[Bucket1Dict]
