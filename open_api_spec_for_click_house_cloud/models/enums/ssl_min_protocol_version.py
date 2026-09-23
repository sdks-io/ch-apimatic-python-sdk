from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SslMinProtocolVersion(str, Enum):
    """Sets the minimum SSL/TLS protocol version allowed for client connections."""

    TL_SV1 = "TLSv1"
    TL_SV1_1 = "TLSv1.1"
    TL_SV1_2 = "TLSv1.2"
    TL_SV1_3 = "TLSv1.3"

    __str__ = str.__str__


SslMinProtocolVersionOrStr: TypeAlias = Annotated[
    SslMinProtocolVersion | str, open_enum_validator(SslMinProtocolVersion)
]
