from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.click_stack_webhook import ClickStackWebhook, ClickStackWebhookDict


class V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse(SdkBaseModel):
    status: Optional[float] = UNSET
    """HTTP status code."""

    request_id: Optional[UUID] = Field(default=UNSET, alias="requestId")
    """Unique id assigned to every request. UUIDv4"""

    result: Optional[ClickStackWebhook] = UNSET


class V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponseDict(TypedDict):
    status: NotRequired[float]
    request_id: NotRequired[UUID]
    result: NotRequired[ClickStackWebhookDict]
