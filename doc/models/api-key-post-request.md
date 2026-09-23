
# Api Key Post Request

*This model accepts additional fields of type Any.*

## Structure

`ApiKeyPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the key. |
| `expire_at` | `datetime` | Optional | Timestamp the key expires. If not present, `null` or is empty the key never expires. ISO-8601. |
| `state` | [`State6`](../../doc/models/state-6.md) | Optional | Initial state of the key: 'enabled', 'disabled'. If not provided the new key will be 'enabled'. |
| `hash_data` | [`ApiKeyHashData`](../../doc/models/api-key-hash-data.md) | Optional | - |
| `roles` | [`List[Role3]`](../../doc/models/role-3.md) | Optional | DEPRECATED. Use `assignedRoleIds` instead. List of roles assigned to the key. Contains at least 1 element. |
| `assigned_role_ids` | `List[uuid\|str]` | Optional | Array of role UUIDs to assign to the API key |
| `ip_access_list` | [`List[IpAccessListEntry]`](../../doc/models/ip-access-list-entry.md) | Optional | List of IP addresses allowed to access the API using this key |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.api_key_hash_data import ApiKeyHashData
from openapispecforclickhousecloud.models.api_key_post_request import ApiKeyPostRequest
from openapispecforclickhousecloud.models.role_3 import Role3
from openapispecforclickhousecloud.models.state_6 import State6

api_key_post_request = ApiKeyPostRequest(
    name='name0',
    expire_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    state=State6.ENABLED,
    hash_data=ApiKeyHashData(
        key_id_hash='keyIdHash4',
        key_id_suffix='keyIdSuffix6',
        key_secret_hash='keySecretHash8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    roles=[
        Role3.QUERY_ENDPOINTS,
        Role3.ADMIN
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

