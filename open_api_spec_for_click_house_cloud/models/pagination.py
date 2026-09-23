from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Pagination(SdkBaseModel):
    total_records: int = Field(alias="totalRecords")
    """Total number of records available."""

    current_cursor: str = Field(alias="currentCursor")
    """Cursor for the current page. Null for the first page."""

    next_cursor: str = Field(alias="nextCursor")
    """Cursor for the next page. Null if there are no more results."""

    limit: int
    """Maximum number of records returned per page."""


class PaginationDict(TypedDict):
    total_records: int
    current_cursor: str
    next_cursor: str
    limit: int
