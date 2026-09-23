
# V1 Organizations Services Clickstack Roles Click Stack Role Id Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickStackRole`](../../doc/models/click-stack-role.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_casl_permission import ClickStackCaslPermission
from openapispecforclickhousecloud.models.click_stack_role import ClickStackRole
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_roles_click_stack_role_id_response import V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse

v_1_organizations_services_clickstack_roles_click_stack_role_id_response = V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse(
    status=200,
    request_id='00002374-0000-0000-0000-000000000000',
    result=ClickStackRole(
        id='id6',
        name='name6',
        permissions=[
            ClickStackCaslPermission(
                action='action4',
                subject='subject2',
                inverted=False,
                integration='integration6',
                conditions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        is_predefined=False,
        description='description6',
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

