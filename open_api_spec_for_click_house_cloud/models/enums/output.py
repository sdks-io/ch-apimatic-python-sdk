from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Output(str, Enum):
    """Output format applied to the number."""

    CURRENCY = "currency"
    PERCENT = "percent"
    BYTE = "byte"
    TIME = "time"
    NUMBER = "number"
    DATA_RATE = "data_rate"
    THROUGHPUT = "throughput"
    DURATION = "duration"

    __str__ = str.__str__


OutputOrStr: TypeAlias = Annotated[Output | str, open_enum_validator(Output)]
