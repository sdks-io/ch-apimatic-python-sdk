
# Click Stack on Click Target Id Variant

*This model accepts additional fields of type Any.*

## Structure

`ClickStackOnClickTargetIdVariant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mode` | `str` | Required, Constant | Target is a single dashboard or log/trace source<br><br>**Value**: `"id"` |
| `id` | `str` | Required | ID of the target source (for search) or dashboard (for dashboard). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_on_click_target_id_variant import ClickStackOnClickTargetIdVariant

click_stack_on_click_target_id_variant = ClickStackOnClickTargetIdVariant(
    id='65f5e4a3b9e77c001a567890',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

