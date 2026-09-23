from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TableEngine(str, Enum):
    """ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null"
    (forward data to materialized views without storing it)."""

    MERGE_TREE = "MergeTree"
    REPLACING_MERGE_TREE = "ReplacingMergeTree"
    NULL = "Null"

    __str__ = str.__str__


TableEngineOrStr: TypeAlias = Annotated[TableEngine | str, open_enum_validator(TableEngine)]
