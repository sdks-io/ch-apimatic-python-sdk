from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.replication_mechanism import ReplicationMechanismOrStr
from .enums.replication_mode import ReplicationModeOrStr


class ClickPipeMySqlpipeSettings(SdkBaseModel):
    sync_interval_seconds: Optional[int] = Field(default=UNSET, alias="syncIntervalSeconds")
    """Interval in seconds to sync data from MySQL during CDC replication."""

    pull_batch_size: Optional[int] = Field(default=UNSET, alias="pullBatchSize")
    """Number of rows to pull in each batch during CDC replication."""

    replication_mode: ReplicationModeOrStr = Field(alias="replicationMode")
    """Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or
    "cdc_only" (CDC without initial snapshot)."""

    replication_mechanism: Optional[ReplicationMechanismOrStr] = Field(default=UNSET, alias="replicationMechanism")
    """MySQL replication mechanism: "GTID" (Global Transaction Identifier) or "FILE_POS" (binary log file and position).
    Defaults to "GTID" if not specified. MariaDB supports "GTID" only. For "FILE_POS" on MySQL, contact support."""

    use_compression: Optional[bool] = Field(default=UNSET, alias="useCompression")
    """Enable compression for the MySQL connection."""

    allow_nullable_columns: Optional[bool] = Field(default=UNSET, alias="allowNullableColumns")
    """Preserve nullability from MySQL in the destination ClickHouse table. When true, columns without NOT NULL
    constraints are created as Nullable(...). When false, all columns are non-nullable and NULL values are replaced with
    the default value for the type. Note: Nullable types have performance overhead in ClickHouse."""

    initial_load_parallelism: Optional[int] = Field(default=UNSET, alias="initialLoadParallelism")
    """Number of parallel workers to use per table in the initial snapshot phase."""

    snapshot_num_rows_per_partition: Optional[int] = Field(default=UNSET, alias="snapshotNumRowsPerPartition")
    """Number of rows per partition during the snapshot phase."""

    snapshot_number_of_parallel_tables: Optional[int] = Field(default=UNSET, alias="snapshotNumberOfParallelTables")
    """Number of tables to snapshot in parallel during the initial load phase."""

    delete_on_merge: Optional[bool] = Field(default=UNSET, alias="deleteOnMerge")
    """Enable hard delete behavior in ReplacingMergeTree for MySQL DELETE operations."""


class ClickPipeMySqlpipeSettingsDict(TypedDict):
    sync_interval_seconds: NotRequired[int]
    pull_batch_size: NotRequired[int]
    replication_mode: ReplicationModeOrStr
    replication_mechanism: NotRequired[ReplicationMechanismOrStr]
    use_compression: NotRequired[bool]
    allow_nullable_columns: NotRequired[bool]
    initial_load_parallelism: NotRequired[int]
    snapshot_num_rows_per_partition: NotRequired[int]
    snapshot_number_of_parallel_tables: NotRequired[int]
    delete_on_merge: NotRequired[bool]
