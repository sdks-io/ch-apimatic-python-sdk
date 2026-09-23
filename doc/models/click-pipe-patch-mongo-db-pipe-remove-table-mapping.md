
# Click Pipe Patch Mongo Db Pipe Remove Table Mapping

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchMongoDbPipeRemoveTableMapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_database_name` | `str` | Required | MongoDB source database name. |
| `source_collection` | `str` | Required | MongoDB source collection name. |
| `target_table` | `str` | Required | ClickHouse target table name. The table will be created automatically if it does not exist. |
| `table_engine` | [`TableEngine`](../../doc/models/table-engine.md) | Optional | ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null" (forward data to materialized views without storing it). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_patch_mongo_db_pipe_remove_table_mapping import ClickPipePatchMongoDbPipeRemoveTableMapping
from openapispecforclickhousecloud.models.table_engine import TableEngine

click_pipe_patch_mongo_db_pipe_remove_table_mapping = ClickPipePatchMongoDbPipeRemoveTableMapping(
    source_database_name='mydb',
    source_collection='users',
    target_table='mydb_users',
    table_engine=TableEngine.REPLACINGMERGETREE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

