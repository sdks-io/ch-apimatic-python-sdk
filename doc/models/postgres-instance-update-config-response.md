
# Postgres Instance Update Config Response

*This model accepts additional fields of type Any.*

## Structure

`PostgresInstanceUpdateConfigResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pg_config` | [`PostgresConfiguration`](../../doc/models/postgres-configuration.md) | Required | Postgres [runtime configuration](https://www.postgresql.org/docs/current/runtime-config.html) configuration. |
| `pg_bouncer_config` | `Dict[str, str]` | Required | PgBouncer [runtime configuration](https://www.pgbouncer.org/config.html) configuration. |
| `message` | `str` | Optional | Informational message about the configuration update, such as restart requirements. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.default_transaction_isolation import DefaultTransactionIsolation
from openapispecforclickhousecloud.models.postgres_configuration import PostgresConfiguration
from openapispecforclickhousecloud.models.postgres_instance_update_config_response import PostgresInstanceUpdateConfigResponse
from openapispecforclickhousecloud.models.ssl_min_protocol_version import SslMinProtocolVersion

postgres_instance_update_config_response = PostgresInstanceUpdateConfigResponse(
    pg_config=PostgresConfiguration(
        max_connections=100,
        default_transaction_isolation=DefaultTransactionIsolation.ENUM_READ_COMMITTED,
        ssl_min_protocol_version=SslMinProtocolVersion.ENUM_TLSV12,
        maintenance_work_mem='String3',
        work_mem='String7'
    ),
    pg_bouncer_config={
        'default_pool_size': '16'
    },
    message='message4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

