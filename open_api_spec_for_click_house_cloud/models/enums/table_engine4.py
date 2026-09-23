from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TableEngine4(str, Enum):
    """Table engine to use for the target table."""

    MERGE_TREE = "MergeTree"
    REPLACING_MERGE_TREE = "ReplacingMergeTree"
    NULL = "Null"

    __str__ = str.__str__


TableEngine4OrStr: TypeAlias = Annotated[TableEngine4 | str, open_enum_validator(TableEngine4)]
