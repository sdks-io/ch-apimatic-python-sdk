from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.table_engine import TableEngineOrStr


class ClickPipePostgresPipeTableMapping(SdkBaseModel):
    source_schema_name: Optional[str] = Field(default=UNSET, alias="sourceSchemaName")
    """PostgreSQL source schema name."""

    source_table: Optional[str] = Field(default=UNSET, alias="sourceTable")
    """PostgreSQL source table name."""

    target_table: Optional[str] = Field(default=UNSET, alias="targetTable")
    """ClickHouse target table name, optionally prefixed with schema name (e.g., "my_schema_my_table"). The table will
    be created automatically if it does not exist. For snapshot mode, the target table must be empty."""

    excluded_columns: Optional[list[str]] = Field(default=UNSET, alias="excludedColumns")
    """List of column names to exclude from replication. Column names must be unique within this list."""

    use_custom_sorting_key: Optional[bool] = Field(default=UNSET, alias="useCustomSortingKey")
    """Whether to use a custom sorting key. If true, sortingKeys must be provided. If false or omitted, the default
    sorting key is the PostgreSQL primary key."""

    sorting_keys: Optional[list[str]] = Field(default=UNSET, alias="sortingKeys")
    """Ordered list of column names to use as the sorting (ORDER BY) key in ClickHouse. Only used when
    useCustomSortingKey is true. Column names must be unique within this list."""

    table_engine: Optional[TableEngineOrStr] = Field(default=UNSET, alias="tableEngine")
    """ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null"
    (forward data to materialized views without storing it)."""

    partition_key: Optional[str] = Field(default=UNSET, alias="partitionKey")
    """Custom partitioning column used for parallel snapshotting. Only beneficial for PostgreSQL 13 (no benefit for
    PG14+, which supports indexed ctid scans). Must be an indexed column of type: ``smallint``, ``integer``, ``bigint``,
    ``timestamp without time zone``, or ``timestamp with time zone``. Unrelated to ClickHouse partitioning."""

    partition_by_expr: Optional[str] = Field(default=UNSET, alias="partitionByExpr")
    """ClickHouse PARTITION BY expression applied to the destination table when ClickPipes creates it."""


class ClickPipePostgresPipeTableMappingDict(TypedDict):
    source_schema_name: NotRequired[str]
    source_table: NotRequired[str]
    target_table: NotRequired[str]
    excluded_columns: NotRequired[list[str]]
    use_custom_sorting_key: NotRequired[bool]
    sorting_keys: NotRequired[list[str]]
    table_engine: NotRequired[TableEngineOrStr]
    partition_key: NotRequired[str]
    partition_by_expr: NotRequired[str]
