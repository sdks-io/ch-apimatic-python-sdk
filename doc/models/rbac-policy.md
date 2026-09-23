
# Rbac Policy

*This model accepts additional fields of type Any.*

## Structure

`RbacPolicy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique policy identifier |
| `role_id` | `str` | Optional | ID of the role this policy belongs to |
| `tenant_id` | `str` | Optional | Tenant resource ID (e.g., organization/uuid) |
| `allow_deny` | [`AllowDeny`](../../doc/models/allow-deny.md) | Optional | Whether this policy allows or denies access |
| `permissions` | `List[str]` | Optional | List of permissions granted or denied by this policy |
| `resources` | `List[str]` | Optional | List of resource IDs this policy applies to (e.g., instance/uuid, instance/*) |
| `tags` | [`RbacPolicyTags`](../../doc/models/rbac-policy-tags.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.allow_deny import AllowDeny
from openapispecforclickhousecloud.models.rbac_policy import RbacPolicy

rbac_policy = RbacPolicy(
    id='id8',
    role_id='roleId2',
    tenant_id='tenantId4',
    allow_deny=AllowDeny.ALLOW,
    permissions=[
        'permissions5'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

