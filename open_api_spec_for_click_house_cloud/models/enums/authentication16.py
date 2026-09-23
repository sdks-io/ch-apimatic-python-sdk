from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication16(str, Enum):
    """Authenticate with a Google Cloud service account JSON key. Defaults to SERVICE_ACCOUNT when omitted."""

    SERVICE_ACCOUNT = "SERVICE_ACCOUNT"

    __str__ = str.__str__


Authentication16OrStr: TypeAlias = Annotated[Authentication16 | str, open_enum_validator(Authentication16)]
