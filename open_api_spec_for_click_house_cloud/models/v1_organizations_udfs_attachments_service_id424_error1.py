from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.code import CodeOrStr
from .enums.service_state import ServiceStateOrStr


class V1OrganizationsUdfsAttachmentsServiceId424Error1(SdkBaseModel):
    error: str
    """Human-readable error message."""

    code: CodeOrStr
    """Reason the attachment could not be started."""

    service_state: ServiceStateOrStr = Field(alias="serviceState")
    """Current state of the service."""

    can_wake: bool = Field(alias="canWake")
    """Whether the service can be woken before retrying the attachment."""

    status: int
    """HTTP status code."""

    request_id: UUID = Field(alias="requestId")
    """Unique id assigned to every request. UUIDv4"""


class V1OrganizationsUdfsAttachmentsServiceId424Error1Dict(TypedDict):
    error: str
    code: CodeOrStr
    service_state: ServiceStateOrStr
    can_wake: bool
    status: int
    request_id: UUID
