from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class UdfUploadSession(SdkBaseModel):
    upload_id: UUID = Field(alias="uploadId")
    """Identifier of the uploaded source archive."""

    upload_url: str = Field(alias="uploadUrl")
    """Presigned URL for uploading the source archive."""

    expires_at: RFC3339DateTime = Field(alias="expiresAt")
    """Presigned-URL expiry timestamp."""


class UdfUploadSessionDict(TypedDict):
    upload_id: UUID
    upload_url: str
    expires_at: RFC3339DateTime
