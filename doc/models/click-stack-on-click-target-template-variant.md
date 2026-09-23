
# Click Stack on Click Target Template Variant

*This model accepts additional fields of type Any.*

## Structure

`ClickStackOnClickTargetTemplateVariant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mode` | `str` | Required, Constant | Target is matched by name against the template.<br><br>**Value**: `"template"` |
| `template` | `str` | Required | Name template rendered against the clicked row; supports `{{column}}` variables. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_on_click_target_template_variant import ClickStackOnClickTargetTemplateVariant

click_stack_on_click_target_template_variant = ClickStackOnClickTargetTemplateVariant(
    template='{{ServiceName}}',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

