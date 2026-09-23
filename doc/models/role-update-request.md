
# Role Update Request

*This model accepts additional fields of type Any.*

## Structure

`RoleUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | New name for the role |
| `actors` | `List[str]` | Optional | New list of actor resource IDs (replaces existing actors) |
| `policies` | [`List[RbacPolicyCreateRequest]`](../../doc/models/rbac-policy-create-request.md) | Optional | New list of policies (replaces existing policies) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.allow_deny import AllowDeny
from openapispecforclickhousecloud.models.rbac_policy_create_request import RbacPolicyCreateRequest
from openapispecforclickhousecloud.models.rbac_policy_tags import RbacPolicyTags
from openapispecforclickhousecloud.models.role_update_request import RoleUpdateRequest
from openapispecforclickhousecloud.models.role_v_2 import RoleV2

role_update_request = RoleUpdateRequest(
    name='name6',
    actors=[
        'actors9',
        'actors0'
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
        ),
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
        ),
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

