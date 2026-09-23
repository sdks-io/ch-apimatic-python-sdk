from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.autoscaling_mode import AutoscalingModeOrStr


class ScalingScheduleEntry(SdkBaseModel):
    id: UUID
    """Unique identifier for this schedule entry."""

    name: str
    """Human-readable label for this schedule entry."""

    weekdays: list[int]
    """Days of the week this entry applies to. 0 = Sunday, 1 = Monday, …, 6 = Saturday."""

    start_hour_utc: int = Field(alias="startHourUtc")
    """UTC hour (0–23) when this entry becomes active (inclusive)."""

    end_hour_utc: int = Field(alias="endHourUtc")
    """UTC hour (1–24) when this entry deactivates (exclusive). Must differ from startHourUtc. Set to 24 to end at
    midnight. Values less than startHourUtc create an overnight window spanning midnight."""

    autoscaling_mode: AutoscalingModeOrStr = Field(alias="autoscalingMode")
    """Autoscaling mode for this entry. "vertical" runs a fixed replica count while memory scales; "horizontal" scales
    the replica count at a fixed per-replica memory. Defaults to "vertical" for entries persisted before the mode was
    exposed."""

    min_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="minReplicaMemoryGb")
    """Minimum memory per replica (Gb) during this window. A range in vertical; in horizontal it equals
    maxReplicaMemoryGb (memory is fixed while the replica count scales)."""

    max_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="maxReplicaMemoryGb")
    """Maximum memory per replica (Gb) during this window. A range in vertical; in horizontal it equals
    minReplicaMemoryGb (memory is fixed while the replica count scales)."""

    min_replicas: Optional[int] = Field(default=UNSET, alias="minReplicas")
    """Minimum number of replicas during this window. For a horizontal entry the replica count scales between
    minReplicas and maxReplicas; for a vertical entry minReplicas and maxReplicas are equal and report the fixed replica
    count (both omitted when the entry stored no count)."""

    max_replicas: Optional[int] = Field(default=UNSET, alias="maxReplicas")
    """Maximum number of replicas during this window. For a horizontal entry the replica count scales between
    minReplicas and maxReplicas; for a vertical entry minReplicas and maxReplicas are equal and report the fixed replica
    count (both omitted when the entry stored no count)."""

    idle_scaling: Optional[bool] = Field(default=UNSET, alias="idleScaling")
    """Whether idle scaling is enabled during this window."""

    idle_timeout_minutes: Optional[int] = Field(default=UNSET, alias="idleTimeoutMinutes")
    """Idle timeout in minutes during this window."""

    is_active_now: bool = Field(alias="isActiveNow")
    """Whether this entry is currently active. Scheduled times are indicative — actions are applied on a best-effort
    basis and may be delayed by a few minutes."""


class ScalingScheduleEntryDict(TypedDict):
    id: UUID
    name: str
    weekdays: list[int]
    start_hour_utc: int
    end_hour_utc: int
    autoscaling_mode: AutoscalingModeOrStr
    min_replica_memory_gb: NotRequired[float]
    max_replica_memory_gb: NotRequired[float]
    min_replicas: NotRequired[int]
    max_replicas: NotRequired[int]
    idle_scaling: NotRequired[bool]
    idle_timeout_minutes: NotRequired[int]
    is_active_now: bool
