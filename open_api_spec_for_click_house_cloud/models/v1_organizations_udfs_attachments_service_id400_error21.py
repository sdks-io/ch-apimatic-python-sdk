from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .issue import Issue, IssueDict


class V1OrganizationsUdfsAttachmentsServiceId400Error21(SdkBaseModel):
    error: str
    """Error message."""

    issues: Optional[list[Issue]] = UNSET
    """Validation issues that caused the request to be rejected."""

    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""


class V1OrganizationsUdfsAttachmentsServiceId400Error21Dict(TypedDict):
    error: str
    issues: NotRequired[list[IssueDict]]
    status: int
    request_id: UUID
