
# V1 Organizations Services Clickstack Roles Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackRolesResponse1`

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
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_roles_response_1 import V1OrganizationsServicesClickstackRolesResponse1

v_1_organizations_services_clickstack_roles_response_1 = V1OrganizationsServicesClickstackRolesResponse1(
    status=200,
    request_id='00000226-0000-0000-0000-000000000000',
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

