from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceScalingPatchRequest(SdkBaseModel):
    min_total_memory_gb: Optional[float] = Field(default=UNSET, alias="minTotalMemoryGb")
    """DEPRECATED - inaccurate for services with non-default numbers of replicas. Use ``minReplicaMemoryGb`` instead.
    Minimum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a
    multiple of 12 and greater than or equal to 24. Always absent for horizontal-autoscaling services (replica count is
    variable)."""

    max_total_memory_gb: Optional[float] = Field(default=UNSET, alias="maxTotalMemoryGb")
    """DEPRECATED - inaccurate for services with non-default numbers of replicas. Use ``maxReplicaMemoryGb`` instead.
    Maximum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a
    multiple of 12 and lower than or equal to 360 for non paid services or 1068 for paid services. Always absent for
    horizontal-autoscaling services (replica count is variable)."""

    num_replicas: Optional[int] = Field(default=UNSET, alias="numReplicas")
    """Number of replicas for the service. The number of replicas must be between 2 and 50 for the first service in a
    warehouse. Services that are created in an existing warehouse can have a number of replicas as low as 1. Further
    restrictions may apply based on your organization's tier and its per-warehouse replica limit. It defaults to 1 for
    the BASIC tier and 3 for the SCALE and ENTERPRISE tiers."""

    idle_scaling: Optional[bool] = Field(default=UNSET, alias="idleScaling")
    """When set to true the service is allowed to scale down to zero when idle. True by default."""

    idle_timeout_minutes: Optional[float] = Field(default=UNSET, alias="idleTimeoutMinutes")
    """Set minimum idling timeout (in minutes). Must be >= 5 minutes."""


class ServiceScalingPatchRequestDict(TypedDict):
    min_total_memory_gb: NotRequired[float]
    max_total_memory_gb: NotRequired[float]
    num_replicas: NotRequired[int]
    idle_scaling: NotRequired[bool]
    idle_timeout_minutes: NotRequired[float]
