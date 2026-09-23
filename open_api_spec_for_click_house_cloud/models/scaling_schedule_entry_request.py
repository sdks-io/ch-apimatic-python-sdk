from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.autoscaling_mode2 import AutoscalingMode2OrStr


class ScalingScheduleEntryRequest(SdkBaseModel):
    name: str
    """Human-readable label for this schedule entry."""

    weekdays: list[int]
    """Days of the week this entry applies to. 0 = Sunday, 1 = Monday, …, 6 = Saturday."""

    start_hour_utc: int = Field(alias="startHourUtc")
    """UTC hour (0–23) when this entry becomes active (inclusive)."""

    end_hour_utc: int = Field(alias="endHourUtc")
    """UTC hour (1–24) when this entry deactivates (exclusive). Must differ from startHourUtc. Set to 24 to end at
    midnight. Values less than startHourUtc create an overnight window spanning midnight."""

    autoscaling_mode: Optional[AutoscalingMode2OrStr] = Field(default=UNSET, alias="autoscalingMode")
    """Autoscaling mode for this entry. "vertical" (the default when omitted) runs a fixed replica count while memory
    scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas
    and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Horizontal requires
    the feature to be enabled for the organization."""

    min_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="minReplicaMemoryGb")
    """Minimum memory per replica (Gb). Optional for vertical entries — provide both bounds for a memory range, or omit
    both to inherit memory from the base scaling config. Required for horizontal (both bounds, equal to
    maxReplicaMemoryGb — memory is fixed while the replica count scales). The upper bound is tier-dependent (lower for
    non-paid organizations) and enforced when the entry is applied."""

    max_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="maxReplicaMemoryGb")
    """Maximum memory per replica (Gb). Optional for vertical entries — provide both bounds for a memory range, or omit
    both to inherit memory from the base scaling config. Required for horizontal (both bounds, equal to
    minReplicaMemoryGb — memory is fixed while the replica count scales). The upper bound is tier-dependent (lower for
    non-paid organizations) and enforced when the entry is applied."""

    num_replicas: Optional[int] = Field(default=UNSET, alias="numReplicas")
    """Fixed replica count for a vertical entry (autoscalingMode "vertical" or omitted). Mutually exclusive with
    minReplicas/maxReplicas. The per-service replica maximum is variable (tier-dependent, configurable per service) and
    enforced when the entry is applied, not at request time."""

    min_replicas: Optional[int] = Field(default=UNSET, alias="minReplicas")
    """Minimum number of replicas. A minReplicas/maxReplicas band scales the replica count in a horizontal entry
    (autoscalingMode "horizontal"); when autoscalingMode is omitted or "vertical", an equal band (minReplicas ===
    maxReplicas) is instead an accepted vertical fixed count and needs no horizontal entitlement. Must be provided
    together with maxReplicas. The per-service replica maximum is variable (tier-dependent, configurable per service)
    and enforced when the entry is applied, not at request time."""

    max_replicas: Optional[int] = Field(default=UNSET, alias="maxReplicas")
    """Maximum number of replicas. A minReplicas/maxReplicas band scales the replica count in a horizontal entry
    (autoscalingMode "horizontal"); when autoscalingMode is omitted or "vertical", an equal band (minReplicas ===
    maxReplicas) is instead an accepted vertical fixed count and needs no horizontal entitlement. Must be provided
    together with minReplicas. The per-service replica maximum is variable (tier-dependent, configurable per service)
    and enforced when the entry is applied, not at request time."""

    idle_scaling: Optional[bool] = Field(default=UNSET, alias="idleScaling")
    """Whether idle scaling is enabled during this window."""

    idle_timeout_minutes: Optional[int] = Field(default=UNSET, alias="idleTimeoutMinutes")
    """Idle timeout in minutes during this window."""


class ScalingScheduleEntryRequestDict(TypedDict):
    name: str
    weekdays: list[int]
    start_hour_utc: int
    end_hour_utc: int
    autoscaling_mode: NotRequired[AutoscalingMode2OrStr]
    min_replica_memory_gb: NotRequired[float]
    max_replica_memory_gb: NotRequired[float]
    num_replicas: NotRequired[int]
    min_replicas: NotRequired[int]
    max_replicas: NotRequired[int]
    idle_scaling: NotRequired[bool]
    idle_timeout_minutes: NotRequired[int]
