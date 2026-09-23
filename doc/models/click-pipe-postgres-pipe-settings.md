
# Click Pipe Postgres Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostgresPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sync_interval_seconds` | `int` | Optional | Interval in seconds to sync data from Postgres during CDC replication.<br><br>**Constraints**: `>= 1` |
| `pull_batch_size` | `int` | Optional | Number of rows to pull in each batch during CDC replication.<br><br>**Constraints**: `>= 1` |
| `publication_name` | `str` | Optional | PostgreSQL publication name to use for CDC replication. If not provided, ClickPipes will create one automatically. |
| `replication_mode` | [`ReplicationMode`](../../doc/models/replication-mode.md) | Optional | Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or "cdc_only" (CDC without initial snapshot). |
| `replication_slot_name` | `str` | Optional | PostgreSQL replication slot name. Only valid for "cdc_only" mode. For "cdc" mode, ClickPipes creates the slot automatically. |
| `allow_nullable_columns` | `bool` | Optional | Preserve nullability from Postgres in the destination ClickHouse table. When true, columns without NOT NULL constraints are created as Nullable(...). When false, all columns are non-nullable and NULL values are replaced with the default value for the type. Note: Nullable types have performance overhead in ClickHouse. |
| `initial_load_parallelism` | `int` | Optional | Number of parallel workers to use per table in the initial snapshot phase.<br><br>**Constraints**: `>= 1` |
| `snapshot_num_rows_per_partition` | `int` | Optional | Number of rows per partition during the snapshot phase.<br><br>**Constraints**: `>= 1000` |
| `snapshot_number_of_parallel_tables` | `int` | Optional | Number of tables to snapshot in parallel during the initial load phase.<br><br>**Constraints**: `>= 1` |
| `enable_failover_slots` | `bool` | Optional | Enable failover support for the replication slot on PG17 and newer. Only applicable when ClickPipes creates the replication slot (i.e., replicationSlotName is NOT provided). |
| `delete_on_merge` | `bool` | Optional | Enable hard delete behavior in ReplacingMergeTree for PostgreSQL DELETE operations. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_postgres_pipe_settings import ClickPipePostgresPipeSettings
from openapispecforclickhousecloud.models.replication_mode import ReplicationMode

click_pipe_postgres_pipe_settings = ClickPipePostgresPipeSettings(
    sync_interval_seconds=60,
    pull_batch_size=1000,
    publication_name='clickpipes_publication',
    replication_mode=ReplicationMode.CDC,
    replication_slot_name='clickpipes_slot',
    allow_nullable_columns=False,
    initial_load_parallelism=1,
    snapshot_num_rows_per_partition=100000,
    snapshot_number_of_parallel_tables=1,
    enable_failover_slots=False,
    delete_on_merge=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

