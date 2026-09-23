
# V1 Organizations Roles Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsRolesResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`RbacRole`](../../doc/models/rbac-role.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.mtype import Type
from openapispecforclickhousecloud.models.rbac_role import RbacRole
from openapispecforclickhousecloud.models.v_1_organizations_roles_response_1 import V1OrganizationsRolesResponse1

v_1_organizations_roles_response_1 = V1OrganizationsRolesResponse1(
    status=200,
    request_id='0000026a-0000-0000-0000-000000000000',
    result=RbacRole(
        id='id6',
        tenant_id='tenantId2',
        owner_id='ownerId8',
        name='name6',
        mtype=Type.SYSTEM,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

