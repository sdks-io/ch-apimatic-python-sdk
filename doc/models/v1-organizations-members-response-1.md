
# V1 Organizations Members Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsMembersResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`Member`](../../doc/models/member.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.member import Member
from openapispecforclickhousecloud.models.role_1 import Role1
from openapispecforclickhousecloud.models.v_1_organizations_members_response_1 import V1OrganizationsMembersResponse1

v_1_organizations_members_response_1 = V1OrganizationsMembersResponse1(
    status=200,
    request_id='00000726-0000-0000-0000-000000000000',
    result=Member(
        user_id='userId6',
        name='name6',
        email='email0',
        role=Role1.ADMIN,
        joined_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

