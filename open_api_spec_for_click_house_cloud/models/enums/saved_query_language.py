from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SavedQueryLanguage(str, Enum):
    """Query language used by savedQuery."""

    SQL = "sql"
    LUCENE = "lucene"

    __str__ = str.__str__


SavedQueryLanguageOrStr: TypeAlias = Annotated[SavedQueryLanguage | str, open_enum_validator(SavedQueryLanguage)]
