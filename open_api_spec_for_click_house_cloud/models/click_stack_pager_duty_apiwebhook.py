from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ClickStackPagerDutyApiwebhook(SdkBaseModel):
    id: str
    """Webhook ID"""

    name: str
    """Webhook name"""

    service: Literal["pagerduty_api"] = "pagerduty_api"
    """Webhook service type"""

    url: Optional[str] = UNSET
    """PagerDuty Events API endpoint URL"""

    description: Optional[str] = UNSET
    """Webhook description, shown in the UI"""

    updated_at: RFC3339DateTime = Field(alias="updatedAt")
    """Last update timestamp"""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """Creation timestamp"""


class ClickStackPagerDutyApiwebhookDict(TypedDict):
    id: str
    name: str
    service: Literal["pagerduty_api"]
    url: NotRequired[str]
    description: NotRequired[str]
    updated_at: RFC3339DateTime
    created_at: RFC3339DateTime
