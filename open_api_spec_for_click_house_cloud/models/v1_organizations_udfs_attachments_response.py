from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .udf_attachment_list_response import UdfAttachmentListResponse, UdfAttachmentListResponseDict


class V1OrganizationsUdfsAttachmentsResponse(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: UdfAttachmentListResponse


class V1OrganizationsUdfsAttachmentsResponseDict(TypedDict):
    status: int
    request_id: UUID
    result: UdfAttachmentListResponseDict
