from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication(str, Enum):
    """Authentication type of the schema registry."""

    PLAIN = "PLAIN"

    __str__ = str.__str__


AuthenticationOrStr: TypeAlias = Annotated[Authentication | str, open_enum_validator(Authentication)]
