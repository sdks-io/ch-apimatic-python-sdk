from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisplayType(str, Enum):
    """Visual representation type for the time series"""

    STACKED_BAR = "stacked_bar"
    LINE = "line"

    __str__ = str.__str__


DisplayTypeOrStr: TypeAlias = Annotated[DisplayType | str, open_enum_validator(DisplayType)]
