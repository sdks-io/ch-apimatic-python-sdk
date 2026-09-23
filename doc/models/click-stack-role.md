
# Click Stack Role

*This model accepts additional fields of type Any.*

## Structure

`ClickStackRole`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Role ID. |
| `name` | `str` | Required | Role name. |
| `description` | `str` | Optional | Human-readable role description. |
| `permissions` | [`List[ClickStackCaslPermission]`](../../doc/models/click-stack-casl-permission.md) | Required | The CASL permissions granted by this role. |
| `is_predefined` | `bool` | Required | Whether this is an immutable predefined/system role. |
| `created_at` | `datetime` | Optional | Creation timestamp. |
| `updated_at` | `datetime` | Optional | Last update timestamp. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_casl_permission import ClickStackCaslPermission
from openapispecforclickhousecloud.models.click_stack_role import ClickStackRole

click_stack_role = ClickStackRole(
    id='507f1f77bcf86cd799439011',
    name='Read Only',
    permissions=[
        ClickStackCaslPermission(
            action='read',
            subject='dashboard',
            inverted=False,
            integration='mongodb',
            conditions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    is_predefined=False,
    description='Read-only access to all resources',
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

