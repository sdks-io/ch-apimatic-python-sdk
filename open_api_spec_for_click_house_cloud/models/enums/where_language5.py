from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WhereLanguage5(str, Enum):
    """Language of the rendered whereTemplate."""

    SQL = "sql"
    LUCENE = "lucene"

    __str__ = str.__str__


WhereLanguage5OrStr: TypeAlias = Annotated[WhereLanguage5 | str, open_enum_validator(WhereLanguage5)]
