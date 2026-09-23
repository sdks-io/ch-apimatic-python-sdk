from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.effective_autoscaling_mode import EffectiveAutoscalingModeOrStr


class CurrentScaling(SdkBaseModel):
    effective_autoscaling_mode: Optional[EffectiveAutoscalingModeOrStr] = Field(
        default=UNSET, alias="effectiveAutoscalingMode"
    )
    """Autoscaling mode currently in effect on the running service. May diverge from the configured baseline mode while
    a schedule entry is active."""

    effective_min_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="effectiveMinReplicaMemoryGb")
    """Minimum memory per replica (Gb) currently applied to the running service. May diverge from the top-level
    ``minReplicaMemoryGb`` baseline while a schedule entry is active."""

    effective_max_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="effectiveMaxReplicaMemoryGb")
    """Maximum memory per replica (Gb) currently applied to the running service. May diverge from the top-level
    ``maxReplicaMemoryGb`` baseline while a schedule entry is active. Reflects the stored value: normally equal to
    ``effectiveMinReplicaMemoryGb`` in horizontal mode, but a legacy service stored with an unequal memory range reports
    the stored bounds as-is."""

    effective_min_replicas: Optional[int] = Field(default=UNSET, alias="effectiveMinReplicas")
    """Minimum number of replicas currently applied to the running service. May diverge from the baseline while a
    schedule entry is active. Reflects the stored value: normally equal to ``effectiveMaxReplicas`` in vertical mode (a
    fixed replica count), but a legacy service stored with an unequal replica range reports the stored bounds as-is."""

    effective_max_replicas: Optional[int] = Field(default=UNSET, alias="effectiveMaxReplicas")
    """Maximum number of replicas currently applied to the running service. May diverge from the baseline while a
    schedule entry is active."""

    effective_idle_scaling: Optional[bool] = Field(default=UNSET, alias="effectiveIdleScaling")
    """Whether idle scaling is currently in effect on the service. May diverge from the top-level ``idleScaling``
    baseline while a schedule entry is active."""

    effective_idle_timeout_minutes: Optional[int] = Field(default=UNSET, alias="effectiveIdleTimeoutMinutes")
    """Idle timeout in minutes currently in effect on the service. May diverge from the top-level ``idleTimeoutMinutes``
    baseline while a schedule entry is active."""

    active_entry_id: Optional[UUID] = Field(default=UNSET, alias="activeEntryId")
    """ID of the schedule entry whose values are currently applied to the service. Absent when no entry is active."""


class CurrentScalingDict(TypedDict):
    effective_autoscaling_mode: NotRequired[EffectiveAutoscalingModeOrStr]
    effective_min_replica_memory_gb: NotRequired[float]
    effective_max_replica_memory_gb: NotRequired[float]
    effective_min_replicas: NotRequired[int]
    effective_max_replicas: NotRequired[int]
    effective_idle_scaling: NotRequired[bool]
    effective_idle_timeout_minutes: NotRequired[int]
    active_entry_id: NotRequired[UUID]
