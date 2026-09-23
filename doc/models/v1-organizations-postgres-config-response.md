
# V1 Organizations Postgres Config Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresConfigResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`PostgresInstanceConfig`](../../doc/models/postgres-instance-config.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_configuration import PostgresConfiguration
from openapispecforclickhousecloud.models.postgres_instance_config import PostgresInstanceConfig
from openapispecforclickhousecloud.models.v_1_organizations_postgres_config_response import V1OrganizationsPostgresConfigResponse

v_1_organizations_postgres_config_response = V1OrganizationsPostgresConfigResponse(
    status=200,
    request_id='00001e08-0000-0000-0000-000000000000',
    result=PostgresInstanceConfig(
        pg_config=PostgresConfiguration(),
        pg_bouncer_config={
            'key0': 'pgBouncerConfig1',
            'key1': 'pgBouncerConfig0'
        },
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

