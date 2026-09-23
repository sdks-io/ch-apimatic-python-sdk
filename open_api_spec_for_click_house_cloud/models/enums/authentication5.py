from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication5(str, Enum):
    """Authentication method to use with the Kinesis stream."""

    IAM_ROLE = "IAM_ROLE"
    IAM_USER = "IAM_USER"

    __str__ = str.__str__


Authentication5OrStr: TypeAlias = Annotated[Authentication5 | str, open_enum_validator(Authentication5)]
