
# Api Key

*This model accepts additional fields of type Any.*

## Structure

`ApiKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique API key ID. |
| `name` | `str` | Optional | Name of the key |
| `state` | [`State4`](../../doc/models/state-4.md) | Optional | State of the key: 'enabled', 'disabled'. |
| `roles` | [`List[Role3]`](../../doc/models/role-3.md) | Optional | DEPRECATED. Use `assignedRoles` instead. List of roles assigned to the key. For organizations that have migrated to custom roles, this field is frozen at the pre-migration value and does not reflect current role assignments. |
| `assigned_roles` | [`List[AssignedRole]`](../../doc/models/assigned-role.md) | Optional | Custom roles and System roles assigned to this API key |
| `key_suffix` | `str` | Optional | Last 4 letters of the key. |
| `created_at` | `datetime` | Optional | Timestamp the key was created. ISO-8601. |
| `expire_at` | `datetime` | Optional | Timestamp the key expires. If not present, `null` or is empty the key never expires. ISO-8601. |
| `used_at` | `datetime` | Optional | Timestamp the key was used last time, with one-minute precision. If not present the key was never used. ISO-8601. |
| `ip_access_list` | [`List[IpAccessListEntry]`](../../doc/models/ip-access-list-entry.md) | Optional | List of IP addresses allowed to access the API using this key |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.api_key import ApiKey
from openapispecforclickhousecloud.models.assigned_role import AssignedRole
from openapispecforclickhousecloud.models.role_3 import Role3
from openapispecforclickhousecloud.models.role_type import RoleType
from openapispecforclickhousecloud.models.state_4 import State4

api_key = ApiKey(
    id='0000058e-0000-0000-0000-000000000000',
    name='name2',
    state=State4.ENABLED,
    roles=[
        Role3.QUERY_ENDPOINTS
    ],
    assigned_roles=[
        AssignedRole(
            role_id='000023ca-0000-0000-0000-000000000000',
            role_name='roleName2',
            role_type=RoleType.SYSTEM,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AssignedRole(
            role_id='000023ca-0000-0000-0000-000000000000',
            role_name='roleName2',
            role_type=RoleType.SYSTEM,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AssignedRole(
            role_id='000023ca-0000-0000-0000-000000000000',
            role_name='roleName2',
            role_type=RoleType.SYSTEM,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

