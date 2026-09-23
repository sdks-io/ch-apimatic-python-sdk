from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PeriodAggFn(str, Enum):
    """Optional period aggregation function for Gauge metrics (e.g., compute the delta over the period)."""

    DELTA = "delta"

    __str__ = str.__str__


PeriodAggFnOrStr: TypeAlias = Annotated[PeriodAggFn | str, open_enum_validator(PeriodAggFn)]
