from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.color1 import Color1OrStr
from .enums.operator1 import Operator1OrStr
from .unions.value import Value, ValueDict


class ClickStackEqualityColorCondition(SdkBaseModel):
    operator: Operator1OrStr
    """Equality comparison operator."""

    value: Value
    """A finite number, or a string up to 200 characters, to compare for equality."""

    color: Color1OrStr
    """Color applied when the rule matches."""

    label: Optional[str] = UNSET
    """Optional label describing the rule."""


class ClickStackEqualityColorConditionDict(TypedDict):
    operator: Operator1OrStr
    value: ValueDict
    color: Color1OrStr
    label: NotRequired[str]
