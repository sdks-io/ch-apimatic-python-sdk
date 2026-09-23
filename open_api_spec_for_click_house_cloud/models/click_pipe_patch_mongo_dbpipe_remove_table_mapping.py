from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.table_engine import TableEngineOrStr


class ClickPipePatchMongoDbpipeRemoveTableMapping(SdkBaseModel):
    source_database_name: str | None = Field(alias="sourceDatabaseName")
    """MongoDB source database name."""

    source_collection: str | None = Field(alias="sourceCollection")
    """MongoDB source collection name."""

    target_table: str | None = Field(alias="targetTable")
    """ClickHouse target table name. The table will be created automatically if it does not exist."""

    table_engine: OptionalNullable[TableEngineOrStr] = Field(default=UNSET, alias="tableEngine")
    """ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null"
    (forward data to materialized views without storing it)."""


class ClickPipePatchMongoDbpipeRemoveTableMappingDict(TypedDict):
    source_database_name: str | None
    source_collection: str | None
    target_table: str | None
    table_engine: NotRequired[TableEngineOrStr | None]
