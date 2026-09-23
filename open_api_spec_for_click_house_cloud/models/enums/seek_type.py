from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SeekType(str, Enum):
    """Starting position strategy for consuming the subscription. The seekTimestamp companion is required only when
    seekType is "timestamp"; setting it for a mismatched seek type is rejected."""

    LATEST = "latest"
    EARLIEST = "earliest"
    TIMESTAMP = "timestamp"

    __str__ = str.__str__


SeekTypeOrStr: TypeAlias = Annotated[SeekType | str, open_enum_validator(SeekType)]
