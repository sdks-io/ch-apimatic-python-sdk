
# Postgres Service Read Replica Request

*This model accepts additional fields of type Any.*

## Structure

`PostgresServiceReadReplicaRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `pg_config` | [`PostgresConfiguration`](../../doc/models/postgres-configuration.md) | Optional | Postgres [runtime configuration](https://www.postgresql.org/docs/current/runtime-config.html) configuration. |
| `pg_bouncer_config` | `Dict[str, str]` | Optional | PgBouncer [runtime configuration](https://www.pgbouncer.org/config.html) configuration. |
| `tags` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use.<br><br>**Constraints**: *Maximum Items*: `50` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.default_transaction_isolation import DefaultTransactionIsolation
from openapispecforclickhousecloud.models.postgres_configuration import PostgresConfiguration
from openapispecforclickhousecloud.models.postgres_service_read_replica_request import PostgresServiceReadReplicaRequest
from openapispecforclickhousecloud.models.resource_tags_v_1 import ResourceTagsV1
from openapispecforclickhousecloud.models.ssl_min_protocol_version import SslMinProtocolVersion

postgres_service_read_replica_request = PostgresServiceReadReplicaRequest(
    name='name6',
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
    tags=[
        ResourceTagsV1(
            key='key0',
            value='value2',
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

