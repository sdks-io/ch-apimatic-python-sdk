from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Protocol1(str, Enum):
    """Endpoint protocol"""

    MYSQL = "mysql"

    __str__ = str.__str__


Protocol1OrStr: TypeAlias = Annotated[Protocol1 | str, open_enum_validator(Protocol1)]
