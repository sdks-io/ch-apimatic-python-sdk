
# Rbac Role

*This model accepts additional fields of type Any.*

## Structure

`RbacRole`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique role identifier |
| `tenant_id` | `str` | Optional | Tenant resource ID (e.g., organization/uuid) |
| `owner_id` | `str` | Optional | Owner resource ID (e.g., organization/uuid) |
| `name` | `str` | Optional | Name of the role |
| `mtype` | [`Type`](../../doc/models/type.md) | Optional | Whether this is a system role or a custom role |
| `actors` | `List[str]` | Optional | List of actor resource IDs assigned to this role (e.g., user/uuid, apiKey/uuid) |
| `policies` | [`List[RbacPolicy]`](../../doc/models/rbac-policy.md) | Optional | List of policies associated with this role |
| `created_at` | `datetime` | Optional | Timestamp when the role was created. ISO-8601. |
| `updated_at` | `datetime` | Optional | Timestamp when the role was last updated. ISO-8601. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.mtype import Type
from openapispecforclickhousecloud.models.rbac_role import RbacRole

rbac_role = RbacRole(
    id='id8',
    tenant_id='tenantId4',
    owner_id='ownerId0',
    name='name8',
    mtype=Type.SYSTEM,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

