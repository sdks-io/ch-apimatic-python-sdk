
# Member Patch Request

*This model accepts additional fields of type Any.*

## Structure

`MemberPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role` | [`Role7`](../../doc/models/role-7.md) | Optional | DEPRECATED. Use `assignedRoleIds` instead. Role of the member in the organization. |
| `assigned_role_ids` | `List[str]` | Optional | List of role IDs to assign to the member |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.member_patch_request import MemberPatchRequest
from openapispecforclickhousecloud.models.role_7 import Role7

member_patch_request = MemberPatchRequest(
    role=Role7.ADMIN,
    assigned_role_ids=[
        'assignedRoleIds0',
        'assignedRoleIds1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

