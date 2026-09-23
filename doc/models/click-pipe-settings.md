
# Click Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `streaming_max_insert_wait_ms` | `int` | Optional | Streaming max insert wait time. Configures the max wait period before inserting data into the ClickHouse.<br><br>**Constraints**: `>= 500`, `<= 60000` |
| `object_storage_concurrency` | `int` | Optional | Object storage concurrency. Number of concurrent file processing threads<br><br>**Constraints**: `>= 1`, `<= 35` |
| `object_storage_polling_interval_ms` | `int` | Optional | Object storage polling interval. Configures the refresh interval for querying continuous ingest for new object storage data<br><br>**Constraints**: `>= 100`, `<= 3600000` |
| `object_storage_max_insert_bytes` | `int` | Optional | Max insert bytes. Number of bytes to process in a single insert batch<br><br>**Constraints**: `>= 524288000`, `<= 10737418240` |
| `object_storage_max_file_count` | `int` | Optional | Max file count. Maximum number of files to process in a single insert batch<br><br>**Constraints**: `>= 1`, `<= 10000` |
| `clickhouse_max_threads` | `int` | Optional | Max threads. Maximum number of concurrent threads for file processing<br><br>**Constraints**: `>= 0`, `<= 64` |
| `clickhouse_max_insert_threads` | `int` | Optional | Max insert threads. Maximum number of concurrent insert threads<br><br>**Constraints**: `>= 0`, `<= 16` |
| `clickhouse_min_insert_block_size_bytes` | `int` | Optional | Min insert block size bytes. Minimum size of data block for insert (in bytes)<br><br>**Constraints**: `>= 0`, `<= 10737418240` |
| `clickhouse_max_download_threads` | `int` | Optional | Max download threads. Maximum number of concurrent download threads<br><br>**Constraints**: `>= 0`, `<= 32` |
| `clickhouse_parallel_distributed_insert_select` | `int` | Optional | Parallel distributed insert select. Parallel distributed insert select setting<br><br>**Constraints**: `>= 0`, `<= 2` |
| `kafka_read_committed` | `bool` | Optional | Kafka Read Committed. Whether Kafka consumers read only committed messages |
| `object_storage_use_cluster_function` | `bool` | Optional | use cluster function. Whether to use ClickHouse cluster function for distributed processing |
| `clickhouse_parallel_view_processing` | `bool` | Optional | parallel view processing. Whether to enable pushing to attached views concurrently instead of sequentially |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_settings import ClickPipeSettings

click_pipe_settings = ClickPipeSettings(
    streaming_max_insert_wait_ms=5000,
    object_storage_concurrency=1,
    object_storage_polling_interval_ms=30000,
    object_storage_max_insert_bytes=10737418240,
    object_storage_max_file_count=100,
    clickhouse_max_threads=8,
    clickhouse_max_insert_threads=1,
    clickhouse_min_insert_block_size_bytes=1073741824,
    clickhouse_max_download_threads=4,
    clickhouse_parallel_distributed_insert_select=2,
    kafka_read_committed=False,
    object_storage_use_cluster_function=True,
    clickhouse_parallel_view_processing=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

