from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WhereLanguage12(str, Enum):
    """Language used for the where filter."""

    LUCENE = "lucene"
    SQL = "sql"

    __str__ = str.__str__


WhereLanguage12OrStr: TypeAlias = Annotated[WhereLanguage12 | str, open_enum_validator(WhereLanguage12)]
