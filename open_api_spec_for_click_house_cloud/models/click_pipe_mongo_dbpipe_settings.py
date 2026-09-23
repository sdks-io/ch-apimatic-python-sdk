from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.replication_mode import ReplicationModeOrStr


class ClickPipeMongoDbpipeSettings(SdkBaseModel):
    sync_interval_seconds: Optional[int] = Field(default=UNSET, alias="syncIntervalSeconds")
    """Interval in seconds to sync data from MongoDB during CDC replication."""

    pull_batch_size: Optional[int] = Field(default=UNSET, alias="pullBatchSize")
    """Number of rows to pull in each batch during CDC replication."""

    replication_mode: ReplicationModeOrStr = Field(alias="replicationMode")
    """Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or
    "cdc_only" (CDC without initial snapshot)."""

    initial_load_parallelism: Optional[int] = Field(default=UNSET, alias="initialLoadParallelism")
    """Number of parallel workers to use per collection in the initial snapshot phase."""

    snapshot_num_rows_per_partition: Optional[int] = Field(default=UNSET, alias="snapshotNumRowsPerPartition")
    """Number of rows per partition during the snapshot phase."""

    snapshot_number_of_parallel_tables: Optional[int] = Field(default=UNSET, alias="snapshotNumberOfParallelTables")
    """Number of collections to snapshot in parallel during the initial load phase."""

    delete_on_merge: Optional[bool] = Field(default=UNSET, alias="deleteOnMerge")
    """Enable hard delete behavior in ReplacingMergeTree for MongoDB DELETE operations."""

    use_json_native_format: Optional[bool] = Field(default=UNSET, alias="useJsonNativeFormat")
    """Store JSON values in native ClickHouse JSON format. When disabled, JSON data is stored as String."""


class ClickPipeMongoDbpipeSettingsDict(TypedDict):
    sync_interval_seconds: NotRequired[int]
    pull_batch_size: NotRequired[int]
    replication_mode: ReplicationModeOrStr
    initial_load_parallelism: NotRequired[int]
    snapshot_num_rows_per_partition: NotRequired[int]
    snapshot_number_of_parallel_tables: NotRequired[int]
    delete_on_merge: NotRequired[bool]
    use_json_native_format: NotRequired[bool]
