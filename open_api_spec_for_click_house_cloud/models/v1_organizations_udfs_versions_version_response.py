from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1OrganizationsUdfsVersionsVersionResponse(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""


class V1OrganizationsUdfsVersionsVersionResponseDict(TypedDict):
    status: int
    request_id: UUID
