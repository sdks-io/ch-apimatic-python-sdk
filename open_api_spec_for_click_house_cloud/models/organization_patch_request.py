from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .organization_private_endpoints_patch import (
    OrganizationPrivateEndpointsPatch,
    OrganizationPrivateEndpointsPatchDict,
)


class OrganizationPatchRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the organization."""

    private_endpoints: Optional[OrganizationPrivateEndpointsPatch] = Field(default=UNSET, alias="privateEndpoints")
    enable_core_dumps: Optional[bool] = Field(default=UNSET, alias="enableCoreDumps")
    """Whether crash reports (core dumps) collection is enabled for services in the organization. When disabled at the
    organization level, individual services cannot enable crash reports."""


class OrganizationPatchRequestDict(TypedDict):
    name: NotRequired[str]
    private_endpoints: NotRequired[OrganizationPrivateEndpointsPatchDict]
    enable_core_dumps: NotRequired[bool]
