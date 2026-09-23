
# Click Pipe Patch Destination

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchDestination`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `columns` | [`List[ClickPipeDestinationColumn]`](../../doc/models/click-pipe-destination-column.md) | Optional | Columns of the destination table. This will not update the table schema, only the ClickPipe configuration. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_destination_column import ClickPipeDestinationColumn
from openapispecforclickhousecloud.models.click_pipe_patch_destination import ClickPipePatchDestination

click_pipe_patch_destination = ClickPipePatchDestination(
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

