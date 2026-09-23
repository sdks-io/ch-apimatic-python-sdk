from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type16 import Type16OrStr


class ClickStackAlertChannelEmail(SdkBaseModel):
    type_: Type16OrStr = Field(alias="type")
    """Channel type. Must be "email" for email alerts."""

    email_recipients: list[str] = Field(alias="emailRecipients")
    """Email recipients for email alerts."""


class ClickStackAlertChannelEmailDict(TypedDict):
    type_: Type16OrStr
    email_recipients: list[str]
