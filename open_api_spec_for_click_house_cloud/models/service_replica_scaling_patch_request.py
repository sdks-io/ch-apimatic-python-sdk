from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.autoscaling_mode6 import AutoscalingMode6OrStr


class ServiceReplicaScalingPatchRequest(SdkBaseModel):
    min_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="minReplicaMemoryGb")
    """Minimum auto-scaling memory in Gb for a single replica. Available only for 'production' services. Must be a
    multiple of 4 and greater than or equal to 8. A range in vertical autoscaling; equal to maxReplicaMemoryGb in
    horizontal."""

    max_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="maxReplicaMemoryGb")
    """Maximum auto-scaling memory in Gb for a single replica. Available only for 'production' services. Must be a
    multiple of 4 and lower than or equal to 120 for non paid services or 356 for paid services. A range in vertical
    autoscaling; equal to minReplicaMemoryGb in horizontal."""

    autoscaling_mode: Optional[AutoscalingMode6OrStr] = Field(default=UNSET, alias="autoscalingMode")
    """Target autoscaling mode. Omit to keep the service on its current mode. "vertical" runs a fixed replica count
    while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between
    minReplicas and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb).
    Switching to horizontal requires the feature to be enabled for the organization."""

    num_replicas: Optional[int] = Field(default=UNSET, alias="numReplicas")
    """Fixed replica count for vertical autoscaling (autoscalingMode "vertical"). Mutually exclusive with
    minReplicas/maxReplicas. When switching to vertical (autoscalingMode "vertical") with numReplicas and no memory, the
    service's stored baseline per-replica memory is kept as the new vertical range. Please contact support to enable
    adjustment of numReplicas."""

    min_replicas: Optional[int] = Field(default=UNSET, alias="minReplicas")
    """Minimum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling
    (autoscalingMode "horizontal"). Must be provided together with maxReplicas. Mutually exclusive with numReplicas.
    Requires horizontal autoscaling to be enabled for the service, unless autoscalingMode is omitted or "vertical" and
    minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal
    entitlement)."""

    max_replicas: Optional[int] = Field(default=UNSET, alias="maxReplicas")
    """Maximum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling
    (autoscalingMode "horizontal"). Must be provided together with minReplicas. Mutually exclusive with numReplicas.
    Requires horizontal autoscaling to be enabled for the service, unless autoscalingMode is omitted or "vertical" and
    minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal
    entitlement)."""

    idle_scaling: Optional[bool] = Field(default=UNSET, alias="idleScaling")
    """When set to true the service is allowed to scale down to zero when idle. True by default."""

    idle_timeout_minutes: Optional[float] = Field(default=UNSET, alias="idleTimeoutMinutes")
    """Set minimum idling timeout (in minutes). Must be >= 5 minutes."""


class ServiceReplicaScalingPatchRequestDict(TypedDict):
    min_replica_memory_gb: NotRequired[float]
    max_replica_memory_gb: NotRequired[float]
    autoscaling_mode: NotRequired[AutoscalingMode6OrStr]
    num_replicas: NotRequired[int]
    min_replicas: NotRequired[int]
    max_replicas: NotRequired[int]
    idle_scaling: NotRequired[bool]
    idle_timeout_minutes: NotRequired[float]
