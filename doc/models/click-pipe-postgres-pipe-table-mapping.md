
# Click Pipe Postgres Pipe Table Mapping

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostgresPipeTableMapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_schema_name` | `str` | Optional | PostgreSQL source schema name. |
| `source_table` | `str` | Optional | PostgreSQL source table name. |
| `target_table` | `str` | Optional | ClickHouse target table name, optionally prefixed with schema name (e.g., "my_schema_my_table"). The table will be created automatically if it does not exist. For snapshot mode, the target table must be empty. |
| `excluded_columns` | `List[str]` | Optional | List of column names to exclude from replication. Column names must be unique within this list.<br><br>**Constraints**: *Unique Items Required* |
| `use_custom_sorting_key` | `bool` | Optional | Whether to use a custom sorting key. If true, sortingKeys must be provided. If false or omitted, the default sorting key is the PostgreSQL primary key. |
| `sorting_keys` | `List[str]` | Optional | Ordered list of column names to use as the sorting (ORDER BY) key in ClickHouse. Only used when useCustomSortingKey is true. Column names must be unique within this list.<br><br>**Constraints**: *Unique Items Required* |
| `table_engine` | [`TableEngine`](../../doc/models/table-engine.md) | Optional | ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null" (forward data to materialized views without storing it). |
| `partition_key` | `str` | Optional | Custom partitioning column used for parallel snapshotting. Only beneficial for PostgreSQL 13 (no benefit for PG14+, which supports indexed ctid scans). Must be an indexed column of type: `smallint`, `integer`, `bigint`, `timestamp without time zone`, or `timestamp with time zone`. Unrelated to ClickHouse partitioning. |
| `partition_by_expr` | `str` | Optional | ClickHouse PARTITION BY expression applied to the destination table when ClickPipes creates it. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_postgres_pipe_table_mapping import ClickPipePostgresPipeTableMapping
from openapispecforclickhousecloud.models.table_engine import TableEngine

click_pipe_postgres_pipe_table_mapping = ClickPipePostgresPipeTableMapping(
    source_schema_name='public',
    source_table='users',
    target_table='public_users',
    excluded_columns=[
        'internal_id',
        'temp_data'
    ],
    use_custom_sorting_key=False,
    sorting_keys=[
        'created_at_date',
        'event_id'
    ],
    table_engine=TableEngine.REPLACINGMERGETREE,
    partition_key='id',
    partition_by_expr='toYYYYMM(created_at)',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

