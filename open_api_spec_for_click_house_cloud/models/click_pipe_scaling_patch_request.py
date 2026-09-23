from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClickPipeScalingPatchRequest(SdkBaseModel):
    replicas: OptionalNullable[int] = UNSET
    """Number of replicas to scale to. Use to scale Kafka pipes."""

    concurrency: OptionalNullable[int] = UNSET
    """Number of concurrency to scale to. Use to scale S3 pipes."""

    replica_cpu_millicores: OptionalNullable[int] = Field(default=UNSET, alias="replicaCpuMillicores")
    """CPU in millicores for each replica. Use to scale streaming pipes."""

    replica_memory_gb: OptionalNullable[float] = Field(default=UNSET, alias="replicaMemoryGb")
    """Memory in GB for each replica. Use to scale streaming pipes."""


class ClickPipeScalingPatchRequestDict(TypedDict):
    replicas: NotRequired[int | None]
    concurrency: NotRequired[int | None]
    replica_cpu_millicores: NotRequired[int | None]
    replica_memory_gb: NotRequired[float | None]
