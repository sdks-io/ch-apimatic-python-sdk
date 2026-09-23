from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .public_query_api_endpoint import PublicQueryApiEndpoint, PublicQueryApiEndpointDict


class V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: PublicQueryApiEndpoint


class V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1Dict(TypedDict):
    status: int
    request_id: UUID
    result: PublicQueryApiEndpointDict
