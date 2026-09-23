
# Click Stack on Click Filter Template

*This model accepts additional fields of type Any.*

## Structure

`ClickStackOnClickFilterTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | `str` | Required, Constant | Filter template kind. Currently only "expressionTemplate" is supported.<br><br>**Value**: `"expressionTemplate"` |
| `expression` | `str` | Required | The column/expression to filter the destination by (e.g. "ServiceName"). |
| `template` | `str` | Required | Value template rendered against the clicked row; supports row column variables in `{{column}}` form (e.g. `{{ServiceName}}`). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_on_click_filter_template import ClickStackOnClickFilterTemplate

click_stack_on_click_filter_template = ClickStackOnClickFilterTemplate(
    expression='ServiceName',
    template='{{ServiceName}}',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

