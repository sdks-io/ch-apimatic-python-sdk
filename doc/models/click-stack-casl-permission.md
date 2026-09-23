
# Click Stack Casl Permission

*This model accepts additional fields of type Any.*

## Structure

`ClickStackCaslPermission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | `str` | Required | The action this permission grants or denies. |
| `subject` | `str` | Required | The resource the action applies to. |
| `inverted` | `bool` | Optional | When true, the rule denies rather than grants the action. |
| `integration` | `str` | Optional | The integration the permission is scoped to. |
| `conditions` | `Any` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_casl_permission import ClickStackCaslPermission

click_stack_casl_permission = ClickStackCaslPermission(
    action='read',
    subject='dashboard',
    inverted=False,
    integration='mongodb',
    conditions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

