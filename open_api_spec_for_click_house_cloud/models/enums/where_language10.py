from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WhereLanguage10(str, Enum):
    """Language of the where condition"""

    SQL = "sql"
    LUCENE = "lucene"

    __str__ = str.__str__


WhereLanguage10OrStr: TypeAlias = Annotated[WhereLanguage10 | str, open_enum_validator(WhereLanguage10)]
