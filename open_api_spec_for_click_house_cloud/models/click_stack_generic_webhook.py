from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ClickStackGenericWebhook(SdkBaseModel):
    id: str
    """Webhook ID"""

    name: str
    """Webhook name"""

    service: Literal["generic"] = "generic"
    """Webhook service type"""

    url: Optional[str] = UNSET
    """Webhook destination URL"""

    description: Optional[str] = UNSET
    """Webhook description, shown in the UI"""

    body: Optional[str] = UNSET
    """Optional request body template"""

    updated_at: RFC3339DateTime = Field(alias="updatedAt")
    """Last update timestamp"""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """Creation timestamp"""


class ClickStackGenericWebhookDict(TypedDict):
    id: str
    name: str
    service: Literal["generic"]
    url: NotRequired[str]
    description: NotRequired[str]
    body: NotRequired[str]
    updated_at: RFC3339DateTime
    created_at: RFC3339DateTime
