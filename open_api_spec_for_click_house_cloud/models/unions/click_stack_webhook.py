from __future__ import annotations

from typing import TypeAlias

from ..click_stack_generic_webhook import ClickStackGenericWebhook, ClickStackGenericWebhookDict
from ..click_stack_incident_iowebhook import ClickStackIncidentIowebhook, ClickStackIncidentIowebhookDict
from ..click_stack_pager_duty_apiwebhook import ClickStackPagerDutyApiwebhook, ClickStackPagerDutyApiwebhookDict
from ..click_stack_slack_apiwebhook import ClickStackSlackApiwebhook, ClickStackSlackApiwebhookDict
from ..click_stack_slack_webhook import ClickStackSlackWebhook, ClickStackSlackWebhookDict

ClickStackWebhook: TypeAlias = (
    ClickStackSlackWebhook
    | ClickStackIncidentIowebhook
    | ClickStackGenericWebhook
    | ClickStackSlackApiwebhook
    | ClickStackPagerDutyApiwebhook
)

ClickStackWebhookDict: TypeAlias = (
    ClickStackSlackWebhookDict
    | ClickStackIncidentIowebhookDict
    | ClickStackGenericWebhookDict
    | ClickStackSlackApiwebhookDict
    | ClickStackPagerDutyApiwebhookDict
)
