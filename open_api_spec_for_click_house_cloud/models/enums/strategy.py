from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Strategy(str, Enum):
    """Offset strategy."""

    FROM_BEGINNING = "from_beginning"
    FROM_LATEST = "from_latest"
    FROM_TIMESTAMP = "from_timestamp"

    __str__ = str.__str__


StrategyOrStr: TypeAlias = Annotated[Strategy | str, open_enum_validator(Strategy)]
