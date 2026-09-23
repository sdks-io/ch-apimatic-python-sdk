from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.autoscaling_mode1 import AutoscalingMode1OrStr


class ScalingScheduleBaseConfig(SdkBaseModel):
    autoscaling_mode: Optional[AutoscalingMode1OrStr] = Field(default=UNSET, alias="autoscalingMode")
    """Autoscaling mode applied when no schedule entry is active. "vertical" runs a fixed replica count while memory
    scales; "horizontal" scales the replica count at a fixed per-replica memory."""

    min_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="minReplicaMemoryGb")
    """Minimum memory per replica (Gb) when no schedule entry is active. Absent for services that do not autoscale
    memory."""

    max_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="maxReplicaMemoryGb")
    """Maximum memory per replica (Gb) when no schedule entry is active. Absent for services that do not autoscale
    memory."""

    min_replicas: Optional[int] = Field(default=UNSET, alias="minReplicas")
    """Minimum number of replicas when no schedule entry is active."""

    max_replicas: Optional[int] = Field(default=UNSET, alias="maxReplicas")
    """Maximum number of replicas when no schedule entry is active."""

    idle_scaling: Optional[bool] = Field(default=UNSET, alias="idleScaling")
    """Whether idle scaling is enabled when no schedule entry is active."""

    idle_timeout_minutes: Optional[int] = Field(default=UNSET, alias="idleTimeoutMinutes")
    """Idle timeout in minutes when no schedule entry is active."""


class ScalingScheduleBaseConfigDict(TypedDict):
    autoscaling_mode: NotRequired[AutoscalingMode1OrStr]
    min_replica_memory_gb: NotRequired[float]
    max_replica_memory_gb: NotRequired[float]
    min_replicas: NotRequired[int]
    max_replicas: NotRequired[int]
    idle_scaling: NotRequired[bool]
    idle_timeout_minutes: NotRequired[int]
