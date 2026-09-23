from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickStackCaslpermission(SdkBaseModel):
    action: str
    """The action this permission grants or denies."""

    subject: str
    """The resource the action applies to."""

    inverted: Optional[bool] = UNSET
    """When true, the rule denies rather than grants the action."""

    integration: Optional[str] = UNSET
    """The integration the permission is scoped to."""

    conditions: Optional[Any] = UNSET


class ClickStackCaslpermissionDict(TypedDict):
    action: str
    subject: str
    inverted: NotRequired[bool]
    integration: NotRequired[str]
    conditions: NotRequired[Any]
