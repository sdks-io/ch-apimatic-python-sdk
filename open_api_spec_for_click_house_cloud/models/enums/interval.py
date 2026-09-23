from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Interval(str, Enum):
    """Evaluation interval for the alert. ``30s`` requires the 30s alert interval feature to be enabled for your
    team."""

    _30S = "30s"
    _1M = "1m"
    _5M = "5m"
    _15M = "15m"
    _30M = "30m"
    _1H = "1h"
    _6H = "6h"
    _12H = "12h"
    _1D = "1d"

    __str__ = str.__str__


IntervalOrStr: TypeAlias = Annotated[Interval | str, open_enum_validator(Interval)]
