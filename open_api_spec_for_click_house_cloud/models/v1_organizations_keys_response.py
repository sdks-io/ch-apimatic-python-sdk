from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_key import ApiKey, ApiKeyDict


class V1OrganizationsKeysResponse(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[list[ApiKey]] = UNSET
    limit: Optional[int] = UNSET
    """Maximum number of results returned in this page."""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """Total number of results across all pages."""

    next_cursor: OptionalNullable[str] = Field(default=UNSET, alias="nextCursor")
    """Cursor for the next page, to be sent as the ``cursor`` query parameter. Null on the last page."""


class V1OrganizationsKeysResponseDict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[list[ApiKeyDict]]
    limit: NotRequired[int]
    total_count: NotRequired[int]
    next_cursor: NotRequired[str | None]
