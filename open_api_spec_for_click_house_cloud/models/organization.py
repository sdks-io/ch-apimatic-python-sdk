from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .byoc_config import ByocConfig, ByocConfigDict
from .organization_private_endpoint import OrganizationPrivateEndpoint, OrganizationPrivateEndpointDict


class Organization(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique organization ID."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """The timestamp the organization was created. ISO-8601."""

    name: Optional[str] = UNSET
    """Name of the organization."""

    private_endpoints: Optional[list[OrganizationPrivateEndpoint]] = Field(default=UNSET, alias="privateEndpoints")
    """List of private endpoints for organization"""

    byoc_config: Optional[list[ByocConfig]] = Field(default=UNSET, alias="byocConfig")
    """BYOC configuration for the organization"""

    enable_core_dumps: Optional[bool] = Field(default=UNSET, alias="enableCoreDumps")
    """Whether crash reports (core dumps) collection is enabled for services in the organization. When disabled at the
    organization level, individual services cannot enable crash reports."""


class OrganizationDict(TypedDict):
    id: NotRequired[UUID]
    created_at: NotRequired[RFC3339DateTime]
    name: NotRequired[str]
    private_endpoints: NotRequired[list[OrganizationPrivateEndpointDict]]
    byoc_config: NotRequired[list[ByocConfigDict]]
    enable_core_dumps: NotRequired[bool]
