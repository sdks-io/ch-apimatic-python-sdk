
# Rbac Policy Create Request

*This model accepts additional fields of type Any.*

## Structure

`RbacPolicyCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_deny` | [`AllowDeny`](../../doc/models/allow-deny.md) | Required | Whether this policy allows or denies access |
| `permissions` | `List[str]` | Required | List of permissions to grant or deny (e.g., ["control-plane:organization:view"]) |
| `resources` | `List[str]` | Required | List of resource IDs this policy applies to (e.g., ["instance/uuid", "instance/*"]) |
| `tags` | [`RbacPolicyTags`](../../doc/models/rbac-policy-tags.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.allow_deny import AllowDeny
from openapispecforclickhousecloud.models.rbac_policy_create_request import RbacPolicyCreateRequest
from openapispecforclickhousecloud.models.rbac_policy_tags import RbacPolicyTags
from openapispecforclickhousecloud.models.role_v_2 import RoleV2

rbac_policy_create_request = RbacPolicyCreateRequest(
    allow_deny=AllowDeny.ALLOW,
    permissions=[
        'permissions5'
    ],
    resources=[
        'resources7',
        'resources8',
        'resources9'
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
```

