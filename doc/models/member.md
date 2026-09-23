
# Member

*This model accepts additional fields of type Any.*

## Structure

`Member`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Optional | Unique user ID. If a user is a member in multiple organizations this ID will stay the same. |
| `name` | `str` | Optional | Name of the member as set a personal user profile. |
| `email` | `str` | Optional | Email of the member as set in personal user profile. |
| `role` | [`Role1`](../../doc/models/role-1.md) | Optional | DEPRECATED. Use `assignedRoles` instead. Role of the member in the organization. For organizations that have migrated to custom roles, this field is frozen at the pre-migration value and does not reflect current role assignments. |
| `joined_at` | `datetime` | Optional | Timestamp the member joined the organization. ISO-8601. |
| `assigned_roles` | [`List[AssignedRole]`](../../doc/models/assigned-role.md) | Optional | Custom roles and System roles assigned to this member |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.member import Member
from openapispecforclickhousecloud.models.role_1 import Role1

member = Member(
    user_id='userId6',
    name='name6',
    email='email0',
    role=Role1.ADMIN,
    joined_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

