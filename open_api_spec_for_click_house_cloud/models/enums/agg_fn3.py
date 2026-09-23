from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AggFn3(str, Enum):
    """Aggregation function to apply. "count" does not require a valueExpression; "quantile" requires a level field
    indicating the desired percentile (e.g., 0.95)."""

    AVG = "avg"
    COUNT = "count"
    COUNT_DISTINCT = "count_distinct"
    LAST_VALUE = "last_value"
    MAX = "max"
    MIN = "min"
    QUANTILE = "quantile"
    SUM = "sum"
    ANY = "any"
    NONE = "none"

    __str__ = str.__str__


AggFn3OrStr: TypeAlias = Annotated[AggFn3 | str, open_enum_validator(AggFn3)]
