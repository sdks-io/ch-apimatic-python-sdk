
# Click Pipe My Sql Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeMySqlPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sync_interval_seconds` | `int` | Optional | Interval in seconds to sync data from MySQL during CDC replication.<br><br>**Constraints**: `>= 1` |
| `pull_batch_size` | `int` | Optional | Number of rows to pull in each batch during CDC replication.<br><br>**Constraints**: `>= 1` |
| `replication_mode` | [`ReplicationMode`](../../doc/models/replication-mode.md) | Required | Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or "cdc_only" (CDC without initial snapshot). |
| `replication_mechanism` | [`ReplicationMechanism`](../../doc/models/replication-mechanism.md) | Optional | MySQL replication mechanism: "GTID" (Global Transaction Identifier) or "FILE_POS" (binary log file and position). Defaults to "GTID" if not specified. MariaDB supports "GTID" only. For "FILE_POS" on MySQL, contact support. |
| `use_compression` | `bool` | Optional | Enable compression for the MySQL connection. |
| `allow_nullable_columns` | `bool` | Optional | Preserve nullability from MySQL in the destination ClickHouse table. When true, columns without NOT NULL constraints are created as Nullable(...). When false, all columns are non-nullable and NULL values are replaced with the default value for the type. Note: Nullable types have performance overhead in ClickHouse. |
| `initial_load_parallelism` | `int` | Optional | Number of parallel workers to use per table in the initial snapshot phase.<br><br>**Constraints**: `>= 1` |
| `snapshot_num_rows_per_partition` | `int` | Optional | Number of rows per partition during the snapshot phase.<br><br>**Constraints**: `>= 1000` |
| `snapshot_number_of_parallel_tables` | `int` | Optional | Number of tables to snapshot in parallel during the initial load phase.<br><br>**Constraints**: `>= 1` |
| `delete_on_merge` | `bool` | Optional | Enable hard delete behavior in ReplacingMergeTree for MySQL DELETE operations. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_my_sql_pipe_settings import ClickPipeMySqlPipeSettings
from openapispecforclickhousecloud.models.replication_mechanism import ReplicationMechanism
from openapispecforclickhousecloud.models.replication_mode import ReplicationMode

click_pipe_my_sql_pipe_settings = ClickPipeMySqlPipeSettings(
    replication_mode=ReplicationMode.CDC,
    sync_interval_seconds=60,
    pull_batch_size=1000,
    replication_mechanism=ReplicationMechanism.GTID,
    use_compression=False,
    allow_nullable_columns=False,
    initial_load_parallelism=1,
    snapshot_num_rows_per_partition=100000,
    snapshot_number_of_parallel_tables=1,
    delete_on_merge=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

