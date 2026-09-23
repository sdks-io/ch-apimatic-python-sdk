
# Click Pipe Destination Column

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeDestinationColumn`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the column. |
| `mtype` | `str` | Optional | Type of the column. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_destination_column import ClickPipeDestinationColumn

click_pipe_destination_column = ClickPipeDestinationColumn(
    name='name0',
    mtype='type0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

