from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Source(str, Enum):
    """Alert source type (tile-based or saved search)."""

    SAVED_SEARCH = "saved_search"
    TILE = "tile"

    __str__ = str.__str__


SourceOrStr: TypeAlias = Annotated[Source | str, open_enum_validator(Source)]
