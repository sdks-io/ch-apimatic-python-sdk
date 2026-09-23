from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DefaultTransactionIsolation(str, Enum):
    """Sets the default transaction isolation level for new transactions."""

    READ_COMMITTED = "read committed"
    REPEATABLE_READ = "repeatable read"
    SERIALIZABLE = "serializable"

    __str__ = str.__str__


DefaultTransactionIsolationOrStr: TypeAlias = Annotated[
    DefaultTransactionIsolation | str, open_enum_validator(DefaultTransactionIsolation)
]
