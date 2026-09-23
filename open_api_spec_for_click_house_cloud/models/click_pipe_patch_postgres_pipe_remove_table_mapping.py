from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.table_engine import TableEngineOrStr


class ClickPipePatchPostgresPipeRemoveTableMapping(SdkBaseModel):
    source_schema_name: OptionalNullable[str] = Field(default=UNSET, alias="sourceSchemaName")
    """PostgreSQL source schema name."""

    source_table: OptionalNullable[str] = Field(default=UNSET, alias="sourceTable")
    """PostgreSQL source table name."""

    target_table: OptionalNullable[str] = Field(default=UNSET, alias="targetTable")
    """ClickHouse target table name, optionally prefixed with schema name (e.g., "my_schema_my_table"). The table will
    be created automatically if it does not exist. For snapshot mode, the target table must be empty."""

    table_engine: OptionalNullable[TableEngineOrStr] = Field(default=UNSET, alias="tableEngine")
    """ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null"
    (forward data to materialized views without storing it)."""

    partition_key: OptionalNullable[str] = Field(default=UNSET, alias="partitionKey")
    """Custom partitioning column used for parallel snapshotting. Only beneficial for PostgreSQL 13 (no benefit for
    PG14+, which supports indexed ctid scans). Must be an indexed column of type: ``smallint``, ``integer``, ``bigint``,
    ``timestamp without time zone``, or ``timestamp with time zone``. Unrelated to ClickHouse partitioning."""

    partition_by_expr: OptionalNullable[str] = Field(default=UNSET, alias="partitionByExpr")
    """ClickHouse PARTITION BY expression applied to the destination table when ClickPipes creates it."""


class ClickPipePatchPostgresPipeRemoveTableMappingDict(TypedDict):
    source_schema_name: NotRequired[str | None]
    source_table: NotRequired[str | None]
    target_table: NotRequired[str | None]
    table_engine: NotRequired[TableEngineOrStr | None]
    partition_key: NotRequired[str | None]
    partition_by_expr: NotRequired[str | None]
