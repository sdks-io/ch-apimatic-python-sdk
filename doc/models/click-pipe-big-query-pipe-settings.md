
# Click Pipe Big Query Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeBigQueryPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `replication_mode` | `str` | Required, Constant | Replication mode. BigQuery only supports snapshot mode.<br><br>**Value**: `"snapshot"` |
| `allow_nullable_columns` | `bool` | Optional | Allow nullable columns in the destination table. |
| `initial_load_parallelism` | `float` | Optional | Number of parallel workers during initial load. |
| `snapshot_num_rows_per_partition` | `float` | Optional | Number of rows to snapshot per partition. |
| `snapshot_number_of_parallel_tables` | `float` | Optional | Number of parallel tables to snapshot. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_big_query_pipe_settings import ClickPipeBigQueryPipeSettings

click_pipe_big_query_pipe_settings = ClickPipeBigQueryPipeSettings(
    allow_nullable_columns=False,
    initial_load_parallelism=111.62,
    snapshot_num_rows_per_partition=38.12,
    snapshot_number_of_parallel_tables=9.8,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

