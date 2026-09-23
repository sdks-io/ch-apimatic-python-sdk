from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Compression(str, Enum):
    """Compression algorithm used for the files."""

    NONE = "none"
    GZIP = "gzip"
    GZ = "gz"
    BROTLI = "brotli"
    BR = "br"
    XZ = "xz"
    LZMA = "LZMA"
    ZSTD = "zstd"
    AUTO = "auto"

    __str__ = str.__str__


CompressionOrStr: TypeAlias = Annotated[Compression | str, open_enum_validator(Compression)]
