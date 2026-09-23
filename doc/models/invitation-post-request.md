
# Invitation Post Request

*This model accepts additional fields of type Any.*

## Structure

`InvitationPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | Email of the invited user. Only a user with this email can join using the invitation. The email is stored in a lowercase form. |
| `role` | [`Role8`](../../doc/models/role-8.md) | Optional | DEPRECATED. Use `assignedRoleIds` instead. Role to assign to the invited user in the organization. |
| `assigned_role_ids` | `List[str]` | Optional | List of role IDs to assign to the invited user when they accept the invitation |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.invitation_post_request import InvitationPostRequest
from openapispecforclickhousecloud.models.role_8 import Role8

invitation_post_request = InvitationPostRequest(
    email='email2',
    role=Role8.ADMIN,
    assigned_role_ids=[
        'assignedRoleIds8',
        'assignedRoleIds7',
        'assignedRoleIds6'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

