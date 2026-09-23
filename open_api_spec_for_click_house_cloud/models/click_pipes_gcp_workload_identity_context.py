from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ClickPipesGcpWorkloadIdentityContext(SdkBaseModel):
    supported: Optional[bool] = UNSET
    """Whether the ClickPipes deployment supports GCP workload identity, which is in Private Preview. The principal
    field identifies the GCP service account used for source access."""

    ready: OptionalNullable[bool] = UNSET
    """Whether the service tenant identity is ready for workload identity authentication."""

    principal: OptionalNullable[str] = UNSET
    """GCP service account used by ClickPipes for workload identity authentication. Grant this service account access to
    customer source resources."""


class ClickPipesGcpWorkloadIdentityContextDict(TypedDict):
    supported: NotRequired[bool]
    ready: NotRequired[bool | None]
    principal: NotRequired[str | None]
