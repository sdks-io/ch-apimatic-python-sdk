
# V1 Organizations Postgres Config Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresConfigResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`PostgresInstanceUpdateConfigResponse`](../../doc/models/postgres-instance-update-config-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_configuration import PostgresConfiguration
from openapispecforclickhousecloud.models.postgres_instance_update_config_response import PostgresInstanceUpdateConfigResponse
from openapispecforclickhousecloud.models.v_1_organizations_postgres_config_response_1 import V1OrganizationsPostgresConfigResponse1

v_1_organizations_postgres_config_response_1 = V1OrganizationsPostgresConfigResponse1(
    status=200,
    request_id='00001c04-0000-0000-0000-000000000000',
    result=PostgresInstanceUpdateConfigResponse(
        pg_config=PostgresConfiguration(),
        pg_bouncer_config={
            'key0': 'pgBouncerConfig1',
            'key1': 'pgBouncerConfig0'
        },
        message='message6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

