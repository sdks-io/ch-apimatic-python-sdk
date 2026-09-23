
# Click Stack Create Role Request

*This model accepts additional fields of type Any.*

## Structure

`ClickStackCreateRoleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Role name. Must be unique within the team and not collide with a predefined role. |
| `description` | `str` | Optional | Human-readable role description. |
| `permissions` | [`List[ClickStackCaslPermission]`](../../doc/models/click-stack-casl-permission.md) | Required | The CASL permissions to grant to the role. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_casl_permission import ClickStackCaslPermission
from openapispecforclickhousecloud.models.click_stack_create_role_request import ClickStackCreateRoleRequest

click_stack_create_role_request = ClickStackCreateRoleRequest(
    name='Deploy Bot',
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
    description='Manages dashboards via Terraform',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

