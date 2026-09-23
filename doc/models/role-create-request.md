
# Role Create Request

*This model accepts additional fields of type Any.*

## Structure

`RoleCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name of the role |
| `actors` | `List[str]` | Required | List of actor resource IDs to assign to this role (e.g., ["user/uuid", "apiKey/uuid"]) |
| `policies` | [`List[RbacPolicyCreateRequest]`](../../doc/models/rbac-policy-create-request.md) | Required | List of policies to create for this role |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.allow_deny import AllowDeny
from openapispecforclickhousecloud.models.rbac_policy_create_request import RbacPolicyCreateRequest
from openapispecforclickhousecloud.models.rbac_policy_tags import RbacPolicyTags
from openapispecforclickhousecloud.models.role_create_request import RoleCreateRequest
from openapispecforclickhousecloud.models.role_v_2 import RoleV2

role_create_request = RoleCreateRequest(
    name='name4',
    actors=[
        'actors3',
        'actors2',
        'actors1'
    ],
    policies=[
        RbacPolicyCreateRequest(
            allow_deny=AllowDeny.ALLOW,
            permissions=[
                'permissions5'
            ],
            resources=[
                'resources3',
                'resources2',
                'resources1'
            ],
            tags=RbacPolicyTags(
                grants=[
                    'grants0',
                    'grants1',
                    'grants2'
                ],
                role_v_2=RoleV2.SQLCONSOLEREADONLY,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
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

