from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.table_engine import TableEngineOrStr


class ClickPipeMongoDbpipeTableMapping(SdkBaseModel):
    source_database_name: str = Field(alias="sourceDatabaseName")
    """MongoDB source database name."""

    source_collection: str = Field(alias="sourceCollection")
    """MongoDB source collection name."""

    target_table: str = Field(alias="targetTable")
    """ClickHouse target table name. The table will be created automatically if it does not exist."""

    table_engine: Optional[TableEngineOrStr] = Field(default=UNSET, alias="tableEngine")
    """ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null"
    (forward data to materialized views without storing it)."""


class ClickPipeMongoDbpipeTableMappingDict(TypedDict):
    source_database_name: str
    source_collection: str
    target_table: str
    table_engine: NotRequired[TableEngineOrStr]
