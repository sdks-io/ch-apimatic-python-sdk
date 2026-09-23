from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceProfile(SdkBaseModel):
    profile: Optional[str] = UNSET
    """Profile name to pass as ``profile`` when creating a service (e.g. 'v1-standard-byoc-4')."""

    cpu_cores: Optional[float] = Field(default=UNSET, alias="cpuCores")
    """Number of vCPUs per replica."""

    memory_gi: Optional[float] = Field(default=UNSET, alias="memoryGi")
    """Memory per replica in GiB. When creating a BYOC service with this profile, minReplicaMemoryGb and
    maxReplicaMemoryGb must both equal this value."""


class ServiceProfileDict(TypedDict):
    profile: NotRequired[str]
    cpu_cores: NotRequired[float]
    memory_gi: NotRequired[float]
