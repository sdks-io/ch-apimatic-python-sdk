from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .organization_cloud_region_private_endpoint_config import (
    OrganizationCloudRegionPrivateEndpointConfig,
    OrganizationCloudRegionPrivateEndpointConfigDict,
)


class V1OrganizationsPrivateEndpointConfigResponse(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[OrganizationCloudRegionPrivateEndpointConfig] = UNSET


class V1OrganizationsPrivateEndpointConfigResponseDict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[OrganizationCloudRegionPrivateEndpointConfigDict]
