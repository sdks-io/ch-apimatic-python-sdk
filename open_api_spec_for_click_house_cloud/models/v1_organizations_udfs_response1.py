from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .udf_list_response import UdfListResponse, UdfListResponseDict


class V1OrganizationsUdfsResponse1(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: UdfListResponse


class V1OrganizationsUdfsResponse1Dict(TypedDict):
    status: int
    request_id: UUID
    result: UdfListResponseDict
