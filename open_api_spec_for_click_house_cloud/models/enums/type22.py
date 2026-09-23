from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type22(str, Enum):
    """Executable UDF type."""

    EXECUTABLE = "executable"
    EXECUTABLE_POOL = "executable_pool"

    __str__ = str.__str__


Type22OrStr: TypeAlias = Annotated[Type22 | str, open_enum_validator(Type22)]
