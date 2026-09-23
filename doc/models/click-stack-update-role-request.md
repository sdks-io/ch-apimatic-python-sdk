
# Click Stack Update Role Request

*This model accepts additional fields of type Any.*

## Structure

`ClickStackUpdateRoleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | New role name. Omit to leave the name unchanged. |
| `description` | `str` | Optional | New role description. |
| `permissions` | [`List[ClickStackCaslPermission]`](../../doc/models/click-stack-casl-permission.md) | Required | The replacement set of CASL permissions for the role. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_casl_permission import ClickStackCaslPermission
from openapispecforclickhousecloud.models.click_stack_update_role_request import ClickStackUpdateRoleRequest

click_stack_update_role_request = ClickStackUpdateRoleRequest(
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
    name='Deploy Bot',
    description='Manages dashboards via Terraform',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

