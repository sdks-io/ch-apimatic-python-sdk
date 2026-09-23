from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1OrganizationsServicesClickpipes400Error1(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    error: Optional[str] = UNSET
    """Detailed error description."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""


class V1OrganizationsServicesClickpipes400Error1Dict(TypedDict):
    status: NotRequired[float]
    error: NotRequired[str]
    request_id: NotRequired[UUID]
