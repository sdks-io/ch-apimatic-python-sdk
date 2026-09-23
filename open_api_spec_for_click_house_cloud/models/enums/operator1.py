from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Operator1(str, Enum):
    """Equality comparison operator."""

    EQ = "eq"
    NEQ = "neq"

    __str__ = str.__str__


Operator1OrStr: TypeAlias = Annotated[Operator1 | str, open_enum_validator(Operator1)]
