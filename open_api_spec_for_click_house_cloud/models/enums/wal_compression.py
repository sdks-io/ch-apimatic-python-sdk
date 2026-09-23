from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalCompression(str, Enum):
    """Compress full-page writes in WAL. Reduces I/O at the cost of CPU. Options vary by PostgreSQL version."""

    OFF = "off"
    ON = "on"
    LZ4 = "lz4"
    ZSTD = "zstd"

    __str__ = str.__str__


WalCompressionOrStr: TypeAlias = Annotated[WalCompression | str, open_enum_validator(WalCompression)]
