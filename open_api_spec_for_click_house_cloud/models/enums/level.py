from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Level(int, Enum):
    """Percentile level; only valid when aggFn is "quantile"."""

    VALUE_0 = 0
    """50th percentile."""

    VALUE_1 = 1
    """90th percentile."""

    VALUE_2 = 2
    """95th percentile."""

    VALUE_3 = 3
    """99th percentile."""

    __str__ = str.__str__


LevelOrInt: TypeAlias = Annotated[Level | int, open_enum_validator(Level)]
