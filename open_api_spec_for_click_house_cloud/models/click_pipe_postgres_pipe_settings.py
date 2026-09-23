from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.replication_mode import ReplicationModeOrStr


class ClickPipePostgresPipeSettings(SdkBaseModel):
    sync_interval_seconds: Optional[int] = Field(default=UNSET, alias="syncIntervalSeconds")
    """Interval in seconds to sync data from Postgres during CDC replication."""

    pull_batch_size: Optional[int] = Field(default=UNSET, alias="pullBatchSize")
    """Number of rows to pull in each batch during CDC replication."""

    publication_name: Optional[str] = Field(default=UNSET, alias="publicationName")
    """PostgreSQL publication name to use for CDC replication. If not provided, ClickPipes will create one
    automatically."""

    replication_mode: Optional[ReplicationModeOrStr] = Field(default=UNSET, alias="replicationMode")
    """Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or
    "cdc_only" (CDC without initial snapshot)."""

    replication_slot_name: Optional[str] = Field(default=UNSET, alias="replicationSlotName")
    """PostgreSQL replication slot name. Only valid for "cdc_only" mode. For "cdc" mode, ClickPipes creates the slot
    automatically."""

    allow_nullable_columns: Optional[bool] = Field(default=UNSET, alias="allowNullableColumns")
    """Preserve nullability from Postgres in the destination ClickHouse table. When true, columns without NOT NULL
    constraints are created as Nullable(...). When false, all columns are non-nullable and NULL values are replaced with
    the default value for the type. Note: Nullable types have performance overhead in ClickHouse."""

    initial_load_parallelism: Optional[int] = Field(default=UNSET, alias="initialLoadParallelism")
    """Number of parallel workers to use per table in the initial snapshot phase."""

    snapshot_num_rows_per_partition: Optional[int] = Field(default=UNSET, alias="snapshotNumRowsPerPartition")
    """Number of rows per partition during the snapshot phase."""

    snapshot_number_of_parallel_tables: Optional[int] = Field(default=UNSET, alias="snapshotNumberOfParallelTables")
    """Number of tables to snapshot in parallel during the initial load phase."""

    enable_failover_slots: Optional[bool] = Field(default=UNSET, alias="enableFailoverSlots")
    """Enable failover support for the replication slot on PG17 and newer. Only applicable when ClickPipes creates the
    replication slot (i.e., replicationSlotName is NOT provided)."""

    delete_on_merge: Optional[bool] = Field(default=UNSET, alias="deleteOnMerge")
    """Enable hard delete behavior in ReplacingMergeTree for PostgreSQL DELETE operations."""


class ClickPipePostgresPipeSettingsDict(TypedDict):
    sync_interval_seconds: NotRequired[int]
    pull_batch_size: NotRequired[int]
    publication_name: NotRequired[str]
    replication_mode: NotRequired[ReplicationModeOrStr]
    replication_slot_name: NotRequired[str]
    allow_nullable_columns: NotRequired[bool]
    initial_load_parallelism: NotRequired[int]
    snapshot_num_rows_per_partition: NotRequired[int]
    snapshot_number_of_parallel_tables: NotRequired[int]
    enable_failover_slots: NotRequired[bool]
    delete_on_merge: NotRequired[bool]
