
# Click Pipe Destination Table Definition

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeDestinationTableDefinition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `engine` | [`ClickPipeDestinationTableEngine`](../../doc/models/click-pipe-destination-table-engine.md) | Optional | - |
| `sorting_key` | `List[str]` | Optional | Sorting key of the destination table. List of columns. |
| `partition_by` | `str` | Optional | Partition key SQL expression. |
| `primary_key` | `str` | Optional | Primary key of SQL expression. |
| `ttl` | `str` | Optional | TTL SQL expression of the destination table.<br><br>**Constraints**: *Minimum Length*: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_destination_table_definition import ClickPipeDestinationTableDefinition
from openapispecforclickhousecloud.models.click_pipe_destination_table_engine import ClickPipeDestinationTableEngine
from openapispecforclickhousecloud.models.type_11 import Type11

click_pipe_destination_table_definition = ClickPipeDestinationTableDefinition(
    engine=ClickPipeDestinationTableEngine(
        mtype=Type11.MERGETREE,
        version_column_id='versionColumnId2',
        column_ids=[
            'columnIds0'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sorting_key=[
        'sortingKey0',
        'sortingKey1',
        'sortingKey2'
    ],
    partition_by='partitionBy0',
    primary_key='primaryKey2',
    ttl='toDateTime(event_time) + INTERVAL 30 DAY',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

