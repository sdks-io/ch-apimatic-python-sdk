from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ClickPipeSettings(SdkBaseModel):
    streaming_max_insert_wait_ms: OptionalNullable[int] = UNSET
    """Streaming max insert wait time. Configures the max wait period before inserting data into the ClickHouse."""

    object_storage_concurrency: OptionalNullable[int] = UNSET
    """Object storage concurrency. Number of concurrent file processing threads"""

    object_storage_polling_interval_ms: OptionalNullable[int] = UNSET
    """Object storage polling interval. Configures the refresh interval for querying continuous ingest for new object
    storage data"""

    object_storage_max_insert_bytes: OptionalNullable[int] = UNSET
    """Max insert bytes. Number of bytes to process in a single insert batch"""

    object_storage_max_file_count: OptionalNullable[int] = UNSET
    """Max file count. Maximum number of files to process in a single insert batch"""

    clickhouse_max_threads: OptionalNullable[int] = UNSET
    """Max threads. Maximum number of concurrent threads for file processing"""

    clickhouse_max_insert_threads: OptionalNullable[int] = UNSET
    """Max insert threads. Maximum number of concurrent insert threads"""

    clickhouse_min_insert_block_size_bytes: OptionalNullable[int] = UNSET
    """Min insert block size bytes. Minimum size of data block for insert (in bytes)"""

    clickhouse_max_download_threads: OptionalNullable[int] = UNSET
    """Max download threads. Maximum number of concurrent download threads"""

    clickhouse_parallel_distributed_insert_select: OptionalNullable[int] = UNSET
    """Parallel distributed insert select. Parallel distributed insert select setting"""

    kafka_read_committed: Optional[bool] = UNSET
    """Kafka Read Committed. Whether Kafka consumers read only committed messages"""

    object_storage_use_cluster_function: OptionalNullable[bool] = UNSET
    """use cluster function. Whether to use ClickHouse cluster function for distributed processing"""

    clickhouse_parallel_view_processing: OptionalNullable[bool] = UNSET
    """parallel view processing. Whether to enable pushing to attached views concurrently instead of sequentially"""


class ClickPipeSettingsDict(TypedDict):
    streaming_max_insert_wait_ms: NotRequired[int | None]
    object_storage_concurrency: NotRequired[int | None]
    object_storage_polling_interval_ms: NotRequired[int | None]
    object_storage_max_insert_bytes: NotRequired[int | None]
    object_storage_max_file_count: NotRequired[int | None]
    clickhouse_max_threads: NotRequired[int | None]
    clickhouse_max_insert_threads: NotRequired[int | None]
    clickhouse_min_insert_block_size_bytes: NotRequired[int | None]
    clickhouse_max_download_threads: NotRequired[int | None]
    clickhouse_parallel_distributed_insert_select: NotRequired[int | None]
    kafka_read_committed: NotRequired[bool]
    object_storage_use_cluster_function: NotRequired[bool | None]
    clickhouse_parallel_view_processing: NotRequired[bool | None]
