from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ClickStackSlackApiwebhook(SdkBaseModel):
    id: str
    """Webhook ID"""

    name: str
    """Webhook name"""

    service: Literal["slack_api"] = "slack_api"
    """Webhook service type"""

    url: Optional[str] = UNSET
    """Slack API endpoint URL"""

    description: Optional[str] = UNSET
    """Webhook description, shown in the UI"""

    updated_at: RFC3339DateTime = Field(alias="updatedAt")
    """Last update timestamp"""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """Creation timestamp"""


class ClickStackSlackApiwebhookDict(TypedDict):
    id: str
    name: str
    service: Literal["slack_api"]
    url: NotRequired[str]
    description: NotRequired[str]
    updated_at: RFC3339DateTime
    created_at: RFC3339DateTime
