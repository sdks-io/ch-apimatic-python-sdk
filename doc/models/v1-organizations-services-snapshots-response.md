
# V1 Organizations Services Snapshots Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesSnapshotsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[Snapshot]`](../../doc/models/snapshot.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.snapshot import Snapshot
from openapispecforclickhousecloud.models.status_2 import Status2
from openapispecforclickhousecloud.models.v_1_organizations_services_snapshots_response import V1OrganizationsServicesSnapshotsResponse

v_1_organizations_services_snapshots_response = V1OrganizationsServicesSnapshotsResponse(
    status=200,
    request_id='000002ee-0000-0000-0000-000000000000',
    result=[
        Snapshot(
            id='000002b8-0000-0000-0000-000000000000',
            status=Status2.DONE,
            service_id='serviceId0',
            started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            finished_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
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

