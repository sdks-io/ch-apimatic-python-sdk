from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickPipeScaling(SdkBaseModel):
    replicas: Optional[int] = UNSET
    """Desired number of replicas. Only for scalable pipes."""

    concurrency: Optional[int] = UNSET
    """Desired number of concurrency. Only for S3 pipes. If set to 0, concurrency is auto-scaled based on the cluster
    memory."""

    replica_cpu_millicores: Optional[int] = Field(default=UNSET, alias="replicaCpuMillicores")
    """CPU in millicores for each replica. Only for streaming pipes."""

    replica_memory_gb: Optional[float] = Field(default=UNSET, alias="replicaMemoryGb")
    """Memory in GB for each replica. Only for streaming pipes."""


class ClickPipeScalingDict(TypedDict):
    replicas: NotRequired[int]
    concurrency: NotRequired[int]
    replica_cpu_millicores: NotRequired[int]
    replica_memory_gb: NotRequired[float]
