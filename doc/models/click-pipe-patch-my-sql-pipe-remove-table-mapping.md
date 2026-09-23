
# Click Pipe Patch My Sql Pipe Remove Table Mapping

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchMySqlPipeRemoveTableMapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_schema_name` | `str` | Required | MySQL source database name. |
| `source_table` | `str` | Required | MySQL source table name. |
| `target_table` | `str` | Required | ClickHouse target table name, optionally prefixed with schema name (e.g., "my_database_my_table"). The table will be created automatically if it does not exist. For snapshot mode, the target table must be empty. |
| `table_engine` | [`TableEngine`](../../doc/models/table-engine.md) | Optional | ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null" (forward data to materialized views without storing it). |
| `partition_key` | `str` | Optional | Custom partitioning column used for parallel snapshotting. Must be an indexed column of an integer, date, datetime or timestamp type. Unrelated to ClickHouse partitioning. |
| `partition_by_expr` | `str` | Optional | ClickHouse PARTITION BY expression applied to the destination table when ClickPipes creates it. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_patch_my_sql_pipe_remove_table_mapping import ClickPipePatchMySqlPipeRemoveTableMapping
from openapispecforclickhousecloud.models.table_engine import TableEngine

click_pipe_patch_my_sql_pipe_remove_table_mapping = ClickPipePatchMySqlPipeRemoveTableMapping(
    source_schema_name='my_database',
    source_table='users',
    target_table='my_database_users',
    table_engine=TableEngine.REPLACINGMERGETREE,
    partition_key='id',
    partition_by_expr='toYYYYMM(created_at)',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

