
# Click Pipe Mongo Db Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeMongoDbPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sync_interval_seconds` | `int` | Optional | Interval in seconds to sync data from MongoDB during CDC replication.<br><br>**Constraints**: `>= 1` |
| `pull_batch_size` | `int` | Optional | Number of rows to pull in each batch during CDC replication.<br><br>**Constraints**: `>= 1` |
| `replication_mode` | [`ReplicationMode`](../../doc/models/replication-mode.md) | Required | Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or "cdc_only" (CDC without initial snapshot). |
| `initial_load_parallelism` | `int` | Optional | Number of parallel workers to use per collection in the initial snapshot phase.<br><br>**Constraints**: `>= 1` |
| `snapshot_num_rows_per_partition` | `int` | Optional | Number of rows per partition during the snapshot phase.<br><br>**Constraints**: `>= 1000` |
| `snapshot_number_of_parallel_tables` | `int` | Optional | Number of collections to snapshot in parallel during the initial load phase.<br><br>**Constraints**: `>= 1` |
| `delete_on_merge` | `bool` | Optional | Enable hard delete behavior in ReplacingMergeTree for MongoDB DELETE operations. |
| `use_json_native_format` | `bool` | Optional | Store JSON values in native ClickHouse JSON format. When disabled, JSON data is stored as String. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_mongo_db_pipe_settings import ClickPipeMongoDbPipeSettings
from openapispecforclickhousecloud.models.replication_mode import ReplicationMode

click_pipe_mongo_db_pipe_settings = ClickPipeMongoDbPipeSettings(
    replication_mode=ReplicationMode.CDC,
    sync_interval_seconds=60,
    pull_batch_size=100000,
    initial_load_parallelism=1,
    snapshot_num_rows_per_partition=100000,
    snapshot_number_of_parallel_tables=1,
    delete_on_merge=False,
    use_json_native_format=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

