from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status3 import Status3OrStr


class UdfAttachment(SdkBaseModel):
    function_name: str = Field(alias="functionName")
    """Name of the UDF."""

    service_id: UUID = Field(alias="serviceId")
    """ID of the attached service."""

    status: Status3OrStr
    """Current attachment lifecycle state."""

    version: int
    """Attached UDF version."""


class UdfAttachmentDict(TypedDict):
    function_name: str
    service_id: UUID
    status: Status3OrStr
    version: int
