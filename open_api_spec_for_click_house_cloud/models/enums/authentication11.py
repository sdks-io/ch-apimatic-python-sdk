from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication11(str, Enum):
    """Authentication method for Postgres connection."""

    BASIC = "basic"
    IAM_ROLE = "IAM_ROLE"

    __str__ = str.__str__


Authentication11OrStr: TypeAlias = Annotated[Authentication11 | str, open_enum_validator(Authentication11)]
