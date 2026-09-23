from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .postgres_service_password_resource import PostgresServicePasswordResource, PostgresServicePasswordResourceDict


class V1OrganizationsPostgresPasswordResponse(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[PostgresServicePasswordResource] = UNSET


class V1OrganizationsPostgresPasswordResponseDict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[PostgresServicePasswordResourceDict]
