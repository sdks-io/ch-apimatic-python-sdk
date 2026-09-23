
# Invitation

*This model accepts additional fields of type Any.*

## Structure

`Invitation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `role` | [`Role2`](../../doc/models/role-2.md) | Optional | DEPRECATED. Use `assignedRoles` instead. Role of the invited user in the organization. For organizations that have migrated to custom roles, this field is frozen at the pre-migration value and does not reflect the role assignment that will be applied. |
| `id` | `uuid\|str` | Optional | Unique invitation ID. |
| `email` | `str` | Optional | Email of the invited user. Only a user with this email can join using the invitation. The email is stored in a lowercase form. |
| `created_at` | `datetime` | Optional | Invitation creation timestamp. ISO-8601. |
| `expire_at` | `datetime` | Optional | Timestamp the invitation expires. ISO-8601. |
| `assigned_roles` | [`List[AssignedRole]`](../../doc/models/assigned-role.md) | Optional | Custom roles and System roles that will be assigned to the user when they accept the invitation |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.invitation import Invitation
from openapispecforclickhousecloud.models.role_2 import Role2

invitation = Invitation(
    role=Role2.ADMIN,
    id='00002526-0000-0000-0000-000000000000',
    email='email6',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expire_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

