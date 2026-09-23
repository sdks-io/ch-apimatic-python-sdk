
# Api Key Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ApiKeyPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the key |
| `roles` | [`List[Role3]`](../../doc/models/role-3.md) | Optional | DEPRECATED. Use `assignedRoleIds` instead. List of roles assigned to the key. |
| `assigned_role_ids` | `List[uuid\|str]` | Optional | Array of role UUIDs to assign to the API key |
| `expire_at` | `datetime` | Optional | Timestamp the key expires. If `null` or is empty the key never expires. ISO-8601. |
| `state` | [`State4`](../../doc/models/state-4.md) | Optional | State of the key: 'enabled', 'disabled'. |
| `ip_access_list` | [`List[IpAccessListEntry]`](../../doc/models/ip-access-list-entry.md) | Optional | List of IP addresses allowed to access the API using this key |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.api_key_patch_request import ApiKeyPatchRequest
from openapispecforclickhousecloud.models.role_3 import Role3
from openapispecforclickhousecloud.models.state_4 import State4

api_key_patch_request = ApiKeyPatchRequest(
    name='name0',
    roles=[
        Role3.DEVELOPER,
        Role3.ADMIN
    ],
    assigned_role_ids=[
        '00000c56-0000-0000-0000-000000000000',
        '00000c57-0000-0000-0000-000000000000'
    ],
    expire_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    state=State4.ENABLED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

