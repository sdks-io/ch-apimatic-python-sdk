
# V1 Organizations Postgres Logs Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresLogsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[PostgresLogEntry]`](../../doc/models/postgres-log-entry.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.postgres_log_entry import PostgresLogEntry
from openapispecforclickhousecloud.models.v_1_organizations_postgres_logs_response import V1OrganizationsPostgresLogsResponse

v_1_organizations_postgres_logs_response = V1OrganizationsPostgresLogsResponse(
    status=200,
    request_id='000001ce-0000-0000-0000-000000000000',
    result=[
        PostgresLogEntry(
            timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            severity='severity6',
            body='body2',
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

