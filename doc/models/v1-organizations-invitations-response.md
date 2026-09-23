
# V1 Organizations Invitations Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsInvitationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[Invitation]`](../../doc/models/invitation.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.invitation import Invitation
from openapispecforclickhousecloud.models.role_2 import Role2
from openapispecforclickhousecloud.models.v_1_organizations_invitations_response import V1OrganizationsInvitationsResponse

v_1_organizations_invitations_response = V1OrganizationsInvitationsResponse(
    status=200,
    request_id='00002112-0000-0000-0000-000000000000',
    result=[
        Invitation(
            role=Role2.ADMIN,
            id='000002b8-0000-0000-0000-000000000000',
            email='email0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            expire_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
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

