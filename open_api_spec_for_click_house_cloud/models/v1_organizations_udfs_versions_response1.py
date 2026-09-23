from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .udf_version_list_response import UdfVersionListResponse, UdfVersionListResponseDict


class V1OrganizationsUdfsVersionsResponse1(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: UdfVersionListResponse


class V1OrganizationsUdfsVersionsResponse1Dict(TypedDict):
    status: int
    request_id: UUID
    result: UdfVersionListResponseDict
