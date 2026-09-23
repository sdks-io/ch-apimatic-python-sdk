
# Postgres Service Post Request

*This model accepts additional fields of type Any.*

## Structure

`PostgresServicePostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `provider` | [`CloudProvider`](../../doc/models/cloud-provider.md) | Required | The cloud provider for a Postgres service. |
| `region` | `str` | Required | The cloud region for a Postgres service. |
| `postgres_version` | [`PostgresMajorVersion`](../../doc/models/postgres-major-version.md) | Optional | - |
| `size` | [`VmSize`](../../doc/models/vm-size.md) | Required | The VM size for a Postgres service. |
| `ha_type` | [`PgHaType`](../../doc/models/pg-ha-type.md) | Optional | Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby, and “sync” for synchronous replication to two standbys. |
| `tags` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use.<br><br>**Constraints**: *Maximum Items*: `50` |
| `pg_config` | [`PostgresConfiguration`](../../doc/models/postgres-configuration.md) | Optional | Postgres [runtime configuration](https://www.postgresql.org/docs/current/runtime-config.html) configuration. |
| `pg_bouncer_config` | `Dict[str, str]` | Optional | PgBouncer [runtime configuration](https://www.pgbouncer.org/config.html) configuration. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider import CloudProvider
from openapispecforclickhousecloud.models.default_transaction_isolation import DefaultTransactionIsolation
from openapispecforclickhousecloud.models.pg_ha_type import PgHaType
from openapispecforclickhousecloud.models.postgres_configuration import PostgresConfiguration
from openapispecforclickhousecloud.models.postgres_major_version import PostgresMajorVersion
from openapispecforclickhousecloud.models.postgres_service_post_request import PostgresServicePostRequest
from openapispecforclickhousecloud.models.resource_tags_v_1 import ResourceTagsV1
from openapispecforclickhousecloud.models.ssl_min_protocol_version import SslMinProtocolVersion
from openapispecforclickhousecloud.models.vm_size import VmSize

postgres_service_post_request = PostgresServicePostRequest(
    name='name6',
    provider=CloudProvider.AWS,
    region='region2',
    size=VmSize.ENUM_I7IE3XLARGE,
    postgres_version=PostgresMajorVersion.POSTGRES18,
    ha_type=PgHaType.SYNC,
    tags=[
        ResourceTagsV1(
            key='key0',
            value='value2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ResourceTagsV1(
            key='key0',
            value='value2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ResourceTagsV1(
            key='key0',
            value='value2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

