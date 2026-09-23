from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type15(str, Enum):
    """Category of the error."""

    QUERY_ERROR = "QUERY_ERROR"
    QUERY_TIMEOUT = "QUERY_TIMEOUT"
    WEBHOOK_ERROR = "WEBHOOK_ERROR"
    INVALID_ALERT = "INVALID_ALERT"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


Type15OrStr: TypeAlias = Annotated[Type15 | str, open_enum_validator(Type15)]
