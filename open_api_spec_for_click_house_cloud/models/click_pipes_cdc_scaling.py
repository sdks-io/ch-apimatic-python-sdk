from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickPipesCdcScaling(SdkBaseModel):
    replica_cpu_millicores: Optional[int] = Field(default=UNSET, alias="replicaCpuMillicores")
    """CPU in millicores for DB ClickPipes."""

    replica_memory_gb: Optional[float] = Field(default=UNSET, alias="replicaMemoryGb")
    """Memory in GiB for DB ClickPipes. Must be 4× the CPU core count."""


class ClickPipesCdcScalingDict(TypedDict):
    replica_cpu_millicores: NotRequired[int]
    replica_memory_gb: NotRequired[float]
