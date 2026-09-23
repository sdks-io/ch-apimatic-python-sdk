
# Click Stack Variable Saved Filter Value

*This model accepts additional fields of type Any.*

## Structure

`ClickStackVariableSavedFilterValue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required, Constant | Filter type.<br><br>**Value**: `"variable"` |
| `name` | `str` | Required | The variableName of the dashboard variable this selection belongs to. Only allowed for variable-enabled filters. |
| `values` | `List[str]` | Required | Selected values |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_variable_saved_filter_value import ClickStackVariableSavedFilterValue

click_stack_variable_saved_filter_value = ClickStackVariableSavedFilterValue(
    name='service',
    values=[
        'hdx-oss-dev-api'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

