from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .postgres_service_list_item import PostgresServiceListItem, PostgresServiceListItemDict


class V1OrganizationsPostgresResponse1(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[list[PostgresServiceListItem]] = UNSET


class V1OrganizationsPostgresResponse1Dict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[list[PostgresServiceListItemDict]]
