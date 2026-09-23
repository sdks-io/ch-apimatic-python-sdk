from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Operator(str, Enum):
    """Numeric comparison operator."""

    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"

    __str__ = str.__str__


OperatorOrStr: TypeAlias = Annotated[Operator | str, open_enum_validator(Operator)]
