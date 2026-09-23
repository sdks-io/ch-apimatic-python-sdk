
# Click Pipe Big Query Pipe Table Mapping

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeBigQueryPipeTableMapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_dataset_name` | `str` | Required | Source BigQuery dataset name. |
| `source_table` | `str` | Required | Source table name. |
| `target_table` | `str` | Required | Target ClickHouse table name. |
| `excluded_columns` | `List[str]` | Optional | Columns to exclude from the target table. |
| `use_custom_sorting_key` | `bool` | Optional | Whether to use a custom sorting key for the target table. |
| `sorting_keys` | `List[str]` | Optional | Ordered list of columns to use as sorting key for the target table. |
| `table_engine` | [`TableEngine4`](../../doc/models/table-engine-4.md) | Optional | Table engine to use for the target table. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_big_query_pipe_table_mapping import ClickPipeBigQueryPipeTableMapping
from openapispecforclickhousecloud.models.table_engine_4 import TableEngine4

click_pipe_big_query_pipe_table_mapping = ClickPipeBigQueryPipeTableMapping(
    source_dataset_name='sourceDatasetName8',
    source_table='sourceTable0',
    target_table='targetTable2',
    excluded_columns=[
        'excludedColumns4',
        'excludedColumns5',
        'excludedColumns6'
    ],
    use_custom_sorting_key=False,
    sorting_keys=[
        'sortingKeys7'
    ],
    table_engine=TableEngine4.NULL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

