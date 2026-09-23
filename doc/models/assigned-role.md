
# Assigned Role

*This model accepts additional fields of type Any.*

## Structure

`AssignedRole`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role_id` | `uuid\|str` | Optional | Unique identifier of the role |
| `role_name` | `str` | Optional | Human-readable name of the role |
| `role_type` | [`RoleType`](../../doc/models/role-type.md) | Optional | Type of role: system (predefined) or custom (organization-defined) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.assigned_role import AssignedRole
from openapispecforclickhousecloud.models.role_type import RoleType

assigned_role = AssignedRole(
    role_id='00000c30-0000-0000-0000-000000000000',
    role_name='roleName0',
    role_type=RoleType.SYSTEM,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

