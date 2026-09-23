from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .udf import Udf, UdfDict


class V1OrganizationsUdfsVersionsResponse(SdkBaseModel):
    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Udf


class V1OrganizationsUdfsVersionsResponseDict(TypedDict):
    status: int
    request_id: UUID
    result: UdfDict
