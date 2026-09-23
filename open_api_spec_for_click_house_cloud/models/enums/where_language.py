from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WhereLanguage(str, Enum):
    """Query language for the where clause"""

    SQL = "sql"
    LUCENE = "lucene"

    __str__ = str.__str__


WhereLanguageOrStr: TypeAlias = Annotated[WhereLanguage | str, open_enum_validator(WhereLanguage)]
