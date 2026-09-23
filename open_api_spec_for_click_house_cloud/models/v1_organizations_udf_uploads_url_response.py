from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .udf_upload_session import UdfUploadSession, UdfUploadSessionDict


class V1OrganizationsUdfUploadsUrlResponse(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: UdfUploadSession


class V1OrganizationsUdfUploadsUrlResponseDict(TypedDict):
    status: int
    request_id: UUID
    result: UdfUploadSessionDict
