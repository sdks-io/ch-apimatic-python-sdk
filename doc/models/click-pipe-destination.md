
# Click Pipe Destination

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeDestination`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `database` | `str` | Optional | Destination database. |
| `table` | `str` | Optional | Destination table. Required field for all pipe types except database pipes (Postgres, MySQL, BigQuery). |
| `managed_table` | `bool` | Optional | Is the table managed by ClickPipes? Required field for all pipe types except database pipes (Postgres, MySQL, BigQuery). |
| `table_definition` | [`ClickPipeDestinationTableDefinition`](../../doc/models/click-pipe-destination-table-definition.md) | Optional | - |
| `columns` | [`List[ClickPipeDestinationColumn]`](../../doc/models/click-pipe-destination-column.md) | Optional | Columns of the destination table. Required field for all pipe types except database pipes (Postgres, MySQL, BigQuery). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_destination import ClickPipeDestination
from openapispecforclickhousecloud.models.click_pipe_destination_column import ClickPipeDestinationColumn
from openapispecforclickhousecloud.models.click_pipe_destination_table_definition import ClickPipeDestinationTableDefinition
from openapispecforclickhousecloud.models.click_pipe_destination_table_engine import ClickPipeDestinationTableEngine
from openapispecforclickhousecloud.models.type_11 import Type11

click_pipe_destination = ClickPipeDestination(
    database='database2',
    table='table4',
    managed_table=False,
    table_definition=ClickPipeDestinationTableDefinition(
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
            'sortingKey0'
        ],
        partition_by='partitionBy0',
        primary_key='primaryKey2',
        ttl='ttl2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    columns=[
        ClickPipeDestinationColumn(
            name='name0',
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickPipeDestinationColumn(
            name='name0',
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickPipeDestinationColumn(
            name='name0',
            mtype='type0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

