from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.severity import SeverityOrStr
from .enums.type17 import Type17OrStr


class ClickStackAlertChannelWebhook(SdkBaseModel):
    type_: Type17OrStr = Field(alias="type")
    """Channel type. Must be "webhook" for webhook alerts."""

    webhook_id: str = Field(alias="webhookId")
    """Webhook destination ID."""

    webhook_service: OptionalNullable[str] = Field(default=UNSET, alias="webhookService")
    """Webhook service type (e.g., slack_api)."""

    slack_channel_id: OptionalNullable[str] = Field(default=UNSET, alias="slackChannelId")
    """Slack channel ID for Slack webhooks."""

    severity: OptionalNullable[SeverityOrStr] = UNSET
    """Severity label used by PagerDuty API webhooks."""


class ClickStackAlertChannelWebhookDict(TypedDict):
    type_: Type17OrStr
    webhook_id: str
    webhook_service: NotRequired[str | None]
    slack_channel_id: NotRequired[str | None]
    severity: NotRequired[SeverityOrStr | None]
