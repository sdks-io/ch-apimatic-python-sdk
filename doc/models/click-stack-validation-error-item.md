
# Click Stack Validation Error Item

*This model accepts additional fields of type Any.*

## Structure

`ClickStackValidationErrorItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | Request part that failed validation. |
| `errors` | `Any` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_validation_error_item import ClickStackValidationErrorItem

click_stack_validation_error_item = ClickStackValidationErrorItem(
    mtype='Body',
    errors=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

