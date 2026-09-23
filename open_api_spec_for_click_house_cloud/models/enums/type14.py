from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type14(str, Enum):
    """Snapshot type. Always "full" — snapshots never chain off a parent."""

    FULL = "full"

    __str__ = str.__str__


Type14OrStr: TypeAlias = Annotated[Type14 | str, open_enum_validator(Type14)]
