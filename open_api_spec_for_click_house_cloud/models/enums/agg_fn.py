from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AggFn(str, Enum):
    """Aggregation function to apply to the field or metric value"""

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


AggFnOrStr: TypeAlias = Annotated[AggFn | str, open_enum_validator(AggFn)]
