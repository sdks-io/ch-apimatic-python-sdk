from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type13(str, Enum):
    """Backup type ("full" or "incremental")."""

    FULL = "full"
    INCREMENTAL = "incremental"

    __str__ = str.__str__


Type13OrStr: TypeAlias = Annotated[Type13 | str, open_enum_validator(Type13)]
