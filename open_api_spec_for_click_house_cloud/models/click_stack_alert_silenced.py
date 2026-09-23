from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ClickStackAlertSilenced(SdkBaseModel):
    by: OptionalNullable[str] = UNSET
    """User ID who silenced the alert."""

    at: Optional[RFC3339DateTime] = UNSET
    """Silence start timestamp."""

    until: Optional[RFC3339DateTime] = UNSET
    """Silence end timestamp."""


class ClickStackAlertSilencedDict(TypedDict):
    by: NotRequired[str | None]
    at: NotRequired[RFC3339DateTime]
    until: NotRequired[RFC3339DateTime]
