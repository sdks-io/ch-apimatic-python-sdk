from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1OrganizationsServicesClickhouseSettingsSettingName500Error1(SdkBaseModel):
    status: Optional[int] = UNSET
    """HTTP status code."""

    error: Optional[str] = UNSET
    """Detailed error description."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""


class V1OrganizationsServicesClickhouseSettingsSettingName500Error1Dict(TypedDict):
    status: NotRequired[int]
    error: NotRequired[str]
    request_id: NotRequired[UUID]
