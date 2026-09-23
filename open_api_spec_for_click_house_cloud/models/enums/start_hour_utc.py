from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StartHourUtc(int, Enum):
    """UTC hour when the upgrade window starts. Must be one of 0, 6, 12, or 18."""

    VALUE_0 = 0
    """Upgrade window starts at 00:00 UTC."""

    VALUE_6 = 6
    """Upgrade window starts at 06:00 UTC."""

    VALUE_12 = 12
    """Upgrade window starts at 12:00 UTC."""

    VALUE_18 = 18
    """Upgrade window starts at 18:00 UTC."""

    __str__ = str.__str__


StartHourUtcOrInt: TypeAlias = Annotated[StartHourUtc | int, open_enum_validator(StartHourUtc)]
