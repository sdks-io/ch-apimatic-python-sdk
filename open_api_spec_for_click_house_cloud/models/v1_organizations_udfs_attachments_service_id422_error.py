from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1OrganizationsUdfsAttachmentsServiceId422Error(SdkBaseModel):
    error: str
    """Human-readable error message."""

    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""


class V1OrganizationsUdfsAttachmentsServiceId422ErrorDict(TypedDict):
    error: str
    status: int
    request_id: UUID
