
# V1 Organizations Keys Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsKeysResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ApiKeyPostResponse`](../../doc/models/api-key-post-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.api_key import ApiKey
from openapispecforclickhousecloud.models.api_key_post_response import ApiKeyPostResponse
from openapispecforclickhousecloud.models.assigned_role import AssignedRole
from openapispecforclickhousecloud.models.role_3 import Role3
from openapispecforclickhousecloud.models.role_type import RoleType
from openapispecforclickhousecloud.models.state_4 import State4
from openapispecforclickhousecloud.models.v_1_organizations_keys_response_1 import V1OrganizationsKeysResponse1

v_1_organizations_keys_response_1 = V1OrganizationsKeysResponse1(
    status=200,
    request_id='00002638-0000-0000-0000-000000000000',
    result=ApiKeyPostResponse(
        key=ApiKey(
            id='00000988-0000-0000-0000-000000000000',
            name='name0',
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
        ),
        key_id='keyId4',
        key_secret='keySecret0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

