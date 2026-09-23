
# V1 Organizations Keys Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsKeysResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[ApiKey]`](../../doc/models/api-key.md) | Optional | - |
| `limit` | `int` | Optional | Maximum number of results returned in this page. |
| `total_count` | `int` | Optional | Total number of results across all pages. |
| `next_cursor` | `str` | Optional | Cursor for the next page, to be sent as the `cursor` query parameter. Null on the last page. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.api_key import ApiKey
from openapispecforclickhousecloud.models.assigned_role import AssignedRole
from openapispecforclickhousecloud.models.role_3 import Role3
from openapispecforclickhousecloud.models.role_type import RoleType
from openapispecforclickhousecloud.models.state_4 import State4
from openapispecforclickhousecloud.models.v_1_organizations_keys_response import V1OrganizationsKeysResponse

v_1_organizations_keys_response = V1OrganizationsKeysResponse(
    status=200,
    request_id='000003ae-0000-0000-0000-000000000000',
    result=[
        ApiKey(
            id='000002b8-0000-0000-0000-000000000000',
            name='name6',
            state=State4.ENABLED,
            roles=[
                Role3.ADMIN,
                Role3.QUERY_ENDPOINTS,
                Role3.DEVELOPER
            ],
            assigned_roles=[
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
        ),
        ApiKey(
            id='000002b8-0000-0000-0000-000000000000',
            name='name6',
            state=State4.ENABLED,
            roles=[
                Role3.ADMIN,
                Role3.QUERY_ENDPOINTS,
                Role3.DEVELOPER
            ],
            assigned_roles=[
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
        ),
        ApiKey(
            id='000002b8-0000-0000-0000-000000000000',
            name='name6',
            state=State4.ENABLED,
            roles=[
                Role3.ADMIN,
                Role3.QUERY_ENDPOINTS,
                Role3.DEVELOPER
            ],
            assigned_roles=[
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
    ],
    limit=208,
    total_count=122,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

