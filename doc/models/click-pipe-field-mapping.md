
# Click Pipe Field Mapping

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeFieldMapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_field` | `str` | Optional | Source field name. |
| `destination_field` | `str` | Optional | Destination field name. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_field_mapping import ClickPipeFieldMapping

click_pipe_field_mapping = ClickPipeFieldMapping(
    source_field='sourceField0',
    destination_field='destinationField2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

