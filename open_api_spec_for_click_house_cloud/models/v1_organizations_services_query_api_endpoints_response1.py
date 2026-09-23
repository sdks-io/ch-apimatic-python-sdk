from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .query_api_endpoint_list_response import QueryApiEndpointListResponse, QueryApiEndpointListResponseDict


class V1OrganizationsServicesQueryApiEndpointsResponse1(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: QueryApiEndpointListResponse


class V1OrganizationsServicesQueryApiEndpointsResponse1Dict(TypedDict):
    status: int
    request_id: UUID
    result: QueryApiEndpointListResponseDict
