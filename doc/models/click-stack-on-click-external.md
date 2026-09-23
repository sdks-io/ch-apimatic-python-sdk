
# Click Stack on Click External

*This model accepts additional fields of type Any.*

## Structure

`ClickStackOnClickExternal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required, Constant | OnClick variant discriminator. Must be "external" for external link-outs.<br><br>**Value**: `"external"` |
| `url_template` | `str` | Required | Handlebars template rendered against the clicked row; supports `{{column}}` variables. The rendered value must be an absolute http(s) URL. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_on_click_external import ClickStackOnClickExternal

click_stack_on_click_external = ClickStackOnClickExternal(
    url_template='https://example.com/d/abc?var-service={{ServiceName}}',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

