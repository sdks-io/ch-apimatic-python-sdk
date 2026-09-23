from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.color1 import Color1OrStr
from .enums.operator import OperatorOrStr


class ClickStackNumericColorCondition(SdkBaseModel):
    operator: OperatorOrStr
    """Numeric comparison operator."""

    value: float
    """Numeric bound the displayed value is compared against. Only finite numbers are accepted (Infinity and NaN are
    rejected)."""

    color: Color1OrStr
    """Color applied when the rule matches."""

    label: Optional[str] = UNSET
    """Optional label describing the rule."""


class ClickStackNumericColorConditionDict(TypedDict):
    operator: OperatorOrStr
    value: float
    color: Color1OrStr
    label: NotRequired[str]
