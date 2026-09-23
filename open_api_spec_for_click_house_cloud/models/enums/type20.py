from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type20(str, Enum):
    """Always ``sql``. Only SQL predicate filters render in the sidebar."""

    SQL = "sql"

    __str__ = str.__str__


Type20OrStr: TypeAlias = Annotated[Type20 | str, open_enum_validator(Type20)]
