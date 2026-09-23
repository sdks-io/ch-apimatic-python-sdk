from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Protocol(str, Enum):
    """Endpoint protocol: 'https', 'nativesecure', 'mysql'."""

    HTTPS = "https"
    NATIVESECURE = "nativesecure"
    MYSQL = "mysql"

    __str__ = str.__str__


ProtocolOrStr: TypeAlias = Annotated[Protocol | str, open_enum_validator(Protocol)]
