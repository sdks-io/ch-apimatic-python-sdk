from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service1 import Service1OrStr


class ClickStackWebhookInput(SdkBaseModel):
    name: str
    """Webhook name. Must be unique per service within the team."""

    service: Service1OrStr
    """Webhook service type."""

    url: str
    """Webhook destination URL."""

    description: Optional[str] = UNSET
    """Webhook description, shown in the UI."""

    body: Optional[str] = UNSET
    """Optional request body template. Only for generic/incidentio; rejected for slack."""

    headers: Optional[dict[str, str]] = UNSET
    query_params: Optional[dict[str, str]] = Field(default=UNSET, alias="queryParams")


class ClickStackWebhookInputDict(TypedDict):
    name: str
    service: Service1OrStr
    url: str
    description: NotRequired[str]
    body: NotRequired[str]
    headers: NotRequired[dict[str, str]]
    query_params: NotRequired[dict[str, str]]
