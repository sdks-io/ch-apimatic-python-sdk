from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .udf_attachment import UdfAttachment, UdfAttachmentDict


class V1OrganizationsUdfsAttachmentsServiceIdResponse(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: UdfAttachment


class V1OrganizationsUdfsAttachmentsServiceIdResponseDict(TypedDict):
    status: int
    request_id: UUID
    result: UdfAttachmentDict
