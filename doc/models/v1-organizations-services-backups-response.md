
# V1 Organizations Services Backups Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesBackupsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[Backup]`](../../doc/models/backup.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.backup import Backup
from openapispecforclickhousecloud.models.status_1 import Status1
from openapispecforclickhousecloud.models.v_1_organizations_services_backups_response import V1OrganizationsServicesBackupsResponse

v_1_organizations_services_backups_response = V1OrganizationsServicesBackupsResponse(
    status=200,
    request_id='00000150-0000-0000-0000-000000000000',
    result=[
        Backup(
            id='000002b8-0000-0000-0000-000000000000',
            status=Status1.DONE,
            service_id='serviceId0',
            started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            finished_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Backup(
            id='000002b8-0000-0000-0000-000000000000',
            status=Status1.DONE,
            service_id='serviceId0',
            started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            finished_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Backup(
            id='000002b8-0000-0000-0000-000000000000',
            status=Status1.DONE,
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

