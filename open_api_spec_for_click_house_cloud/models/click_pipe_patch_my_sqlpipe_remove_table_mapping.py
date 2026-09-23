from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.table_engine import TableEngineOrStr


class ClickPipePatchMySqlpipeRemoveTableMapping(SdkBaseModel):
    source_schema_name: str | None = Field(alias="sourceSchemaName")
    """MySQL source database name."""

    source_table: str | None = Field(alias="sourceTable")
    """MySQL source table name."""

    target_table: str | None = Field(alias="targetTable")
    """ClickHouse target table name, optionally prefixed with schema name (e.g., "my_database_my_table"). The table will
    be created automatically if it does not exist. For snapshot mode, the target table must be empty."""

    table_engine: OptionalNullable[TableEngineOrStr] = Field(default=UNSET, alias="tableEngine")
    """ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null"
    (forward data to materialized views without storing it)."""

    partition_key: OptionalNullable[str] = Field(default=UNSET, alias="partitionKey")
    """Custom partitioning column used for parallel snapshotting. Must be an indexed column of an integer, date,
    datetime or timestamp type. Unrelated to ClickHouse partitioning."""

    partition_by_expr: OptionalNullable[str] = Field(default=UNSET, alias="partitionByExpr")
    """ClickHouse PARTITION BY expression applied to the destination table when ClickPipes creates it."""


class ClickPipePatchMySqlpipeRemoveTableMappingDict(TypedDict):
    source_schema_name: str | None
    source_table: str | None
    target_table: str | None
    table_engine: NotRequired[TableEngineOrStr | None]
    partition_key: NotRequired[str | None]
    partition_by_expr: NotRequired[str | None]
