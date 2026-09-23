
# Rbac Policy Tags

*This model accepts additional fields of type Any.*

## Structure

`RbacPolicyTags`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grants` | `List[str]` | Optional | Optional list of database grants (e.g., database names) |
| `role_v_2` | [`RoleV2`](../../doc/models/role-v2.md) | Optional | Optional SQL console role type |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.rbac_policy_tags import RbacPolicyTags
from openapispecforclickhousecloud.models.role_v_2 import RoleV2

rbac_policy_tags = RbacPolicyTags(
    grants=[
        'grants4',
        'grants5'
    ],
    role_v_2=RoleV2.SQLCONSOLEREADONLY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

