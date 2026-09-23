from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State3(str, Enum):
    """Current alert state."""

    ALERT = "ALERT"
    OK = "OK"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    DISABLED = "DISABLED"
    PENDING = "PENDING"

    __str__ = str.__str__


State3OrStr: TypeAlias = Annotated[State3 | str, open_enum_validator(State3)]
