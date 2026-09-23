
# Api Key Post Response

*This model accepts additional fields of type Any.*

## Structure

`ApiKeyPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | [`ApiKey`](../../doc/models/api-key.md) | Optional | - |
| `key_id` | `str` | Optional | Generated key ID. Provided only if there was no 'hashData' in the request. |
| `key_secret` | `str` | Optional | Generated key secret. Provided only if there was no 'hashData' in the request. |
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

api_key_post_response = ApiKeyPostResponse(
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
    key_id='keyId0',
    key_secret='keySecret4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

