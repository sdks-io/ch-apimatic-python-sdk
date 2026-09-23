from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type19(str, Enum):
    """Sparkline shape."""

    LINE = "line"
    AREA = "area"

    __str__ = str.__str__


Type19OrStr: TypeAlias = Annotated[Type19 | str, open_enum_validator(Type19)]
