from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication13(str, Enum):
    """Authentication method for MySQL connection."""

    BASIC = "basic"
    IAM_ROLE = "IAM_ROLE"

    __str__ = str.__str__


Authentication13OrStr: TypeAlias = Annotated[Authentication13 | str, open_enum_validator(Authentication13)]
