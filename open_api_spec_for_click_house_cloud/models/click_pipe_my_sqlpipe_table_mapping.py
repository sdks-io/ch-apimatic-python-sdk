from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.table_engine import TableEngineOrStr


class ClickPipeMySqlpipeTableMapping(SdkBaseModel):
    source_schema_name: str = Field(alias="sourceSchemaName")
    """MySQL source database name."""

    source_table: str = Field(alias="sourceTable")
    """MySQL source table name."""

    target_table: str = Field(alias="targetTable")
    """ClickHouse target table name, optionally prefixed with schema name (e.g., "my_database_my_table"). The table will
    be created automatically if it does not exist. For snapshot mode, the target table must be empty."""

    excluded_columns: Optional[list[str]] = Field(default=UNSET, alias="excludedColumns")
    """List of column names to exclude from replication. Column names must be unique within this list."""

    use_custom_sorting_key: Optional[bool] = Field(default=UNSET, alias="useCustomSortingKey")
    """Whether to use a custom sorting key. If true, sortingKeys must be provided. If false or omitted, the default
    sorting key is the MySQL primary key."""

    sorting_keys: Optional[list[str]] = Field(default=UNSET, alias="sortingKeys")
    """Ordered list of column names to use as the sorting (ORDER BY) key in ClickHouse. Only used when
    useCustomSortingKey is true. Column names must be unique within this list."""

    table_engine: Optional[TableEngineOrStr] = Field(default=UNSET, alias="tableEngine")
    """ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null"
    (forward data to materialized views without storing it)."""

    partition_key: Optional[str] = Field(default=UNSET, alias="partitionKey")
    """Custom partitioning column used for parallel snapshotting. Must be an indexed column of an integer, date,
    datetime or timestamp type. Unrelated to ClickHouse partitioning."""

    partition_by_expr: Optional[str] = Field(default=UNSET, alias="partitionByExpr")
    """ClickHouse PARTITION BY expression applied to the destination table when ClickPipes creates it."""


class ClickPipeMySqlpipeTableMappingDict(TypedDict):
    source_schema_name: str
    source_table: str
    target_table: str
    excluded_columns: NotRequired[list[str]]
    use_custom_sorting_key: NotRequired[bool]
    sorting_keys: NotRequired[list[str]]
    table_engine: NotRequired[TableEngineOrStr]
    partition_key: NotRequired[str]
    partition_by_expr: NotRequired[str]
