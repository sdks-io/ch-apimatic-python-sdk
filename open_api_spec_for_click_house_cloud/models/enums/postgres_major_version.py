from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PostgresMajorVersion(str, Enum):
    _18 = "18"
    """Postgres major version 18."""

    _17 = "17"
    """Postgres major version 17."""

    __str__ = str.__str__


PostgresMajorVersionOrStr: TypeAlias = Annotated[PostgresMajorVersion | str, open_enum_validator(PostgresMajorVersion)]
