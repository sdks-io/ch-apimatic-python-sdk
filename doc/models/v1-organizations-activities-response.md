
# V1 Organizations Activities Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsActivitiesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[Activity]`](../../doc/models/activity.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.activity import Activity
from openapispecforclickhousecloud.models.actor_type import ActorType
from openapispecforclickhousecloud.models.type_12 import Type12
from openapispecforclickhousecloud.models.v_1_organizations_activities_response import V1OrganizationsActivitiesResponse

v_1_organizations_activities_response = V1OrganizationsActivitiesResponse(
    status=200,
    request_id='000003a8-0000-0000-0000-000000000000',
    result=[
        Activity(
            id='id6',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            mtype=Type12.SERVICE_RUNNING,
            actor_type=ActorType.USER,
            actor_id='actorId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Activity(
            id='id6',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            mtype=Type12.SERVICE_RUNNING,
            actor_type=ActorType.USER,
            actor_id='actorId6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Activity(
            id='id6',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            mtype=Type12.SERVICE_RUNNING,
            actor_type=ActorType.USER,
            actor_id='actorId6',
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

