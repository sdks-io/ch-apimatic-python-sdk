from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipes_gcp_workload_identity_context import (
    ClickPipesGcpWorkloadIdentityContext,
    ClickPipesGcpWorkloadIdentityContextDict,
)


class ClickPipesServiceContext(SdkBaseModel):
    gcp_workload_identity: Optional[ClickPipesGcpWorkloadIdentityContext] = Field(
        default=UNSET, alias="gcpWorkloadIdentity"
    )


class ClickPipesServiceContextDict(TypedDict):
    gcp_workload_identity: NotRequired[ClickPipesGcpWorkloadIdentityContextDict]
