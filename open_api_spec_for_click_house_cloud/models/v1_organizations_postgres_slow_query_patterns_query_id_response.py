from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .postgres_slow_query_pattern_detail import PostgresSlowQueryPatternDetail, PostgresSlowQueryPatternDetailDict


class V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[PostgresSlowQueryPatternDetail] = UNSET


class V1OrganizationsPostgresSlowQueryPatternsQueryIdResponseDict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[PostgresSlowQueryPatternDetailDict]
