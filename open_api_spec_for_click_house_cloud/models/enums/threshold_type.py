from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ThresholdType(str, Enum):
    """Threshold comparison direction."""

    ABOVE = "above"
    BELOW = "below"
    ABOVE_EXCLUSIVE = "above_exclusive"
    BELOW_OR_EQUAL = "below_or_equal"
    EQUAL = "equal"
    NOT_EQUAL = "not_equal"
    BETWEEN = "between"
    NOT_BETWEEN = "not_between"

    __str__ = str.__str__


ThresholdTypeOrStr: TypeAlias = Annotated[ThresholdType | str, open_enum_validator(ThresholdType)]
