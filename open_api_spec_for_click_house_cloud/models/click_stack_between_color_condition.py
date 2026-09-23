from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.color1 import Color1OrStr


class ClickStackBetweenColorCondition(SdkBaseModel):
    operator: Literal["between"] = "between"
    """Range comparison operator."""

    value: list[float]
    """Inclusive [min, max] range. Both bounds must be finite numbers."""

    color: Color1OrStr
    """Color applied when the rule matches."""

    label: Optional[str] = UNSET
    """Optional label describing the rule."""


class ClickStackBetweenColorConditionDict(TypedDict):
    operator: Literal["between"]
    value: list[float]
    color: Color1OrStr
    label: NotRequired[str]
