
# Postgres Service

*This model accepts additional fields of type Any.*

## Structure

`PostgresService`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `provider` | [`CloudProvider`](../../doc/models/cloud-provider.md) | Optional | The cloud provider for a Postgres service. |
| `region` | `str` | Optional | The cloud region for a Postgres service. |
| `postgres_version` | [`PostgresMajorVersion`](../../doc/models/postgres-major-version.md) | Optional | - |
| `size` | [`VmSize`](../../doc/models/vm-size.md) | Optional | The VM size for a Postgres service. |
| `ha_type` | [`PgHaType`](../../doc/models/pg-ha-type.md) | Optional | Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby, and “sync” for synchronous replication to two standbys. |
| `tags` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use.<br><br>**Constraints**: *Maximum Items*: `50` |
| `id` | `uuid\|str` | Optional | - |
| `storage_size` | `int` | Optional | The storage size, in GiB, which must be supported by the specified `size`. |
| `state` | [`PostgresServiceState`](../../doc/models/postgres-service-state.md) | Optional | Current state of the service |
| `created_at` | `datetime` | Optional | - |
| `is_primary` | `bool` | Optional | True if this service is the primary service in the data warehouse<br><br>**Default**: `False` |
| `connection_string` | `str` | Optional | Connection string to the Postgres service. Embeds the service password, so it is only returned when the service is created or its password is reset. Omitted from every other response when Postgres credential redaction is enabled for the organization. Not guaranteed to be present — treat as optional. |
| `username` | `str` | Optional | Username for the Postgres service |
| `password` | `str` | Optional | Password for the Postgres service. Only returned when the service is created or its password is reset. Omitted from every other response when Postgres credential redaction is enabled for the organization. Not guaranteed to be present — treat as optional. |
| `hostname` | `str` | Optional | Hostname for the Postgres service |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider import CloudProvider
from openapispecforclickhousecloud.models.postgres_major_version import PostgresMajorVersion
from openapispecforclickhousecloud.models.postgres_service import PostgresService
from openapispecforclickhousecloud.models.vm_size import VmSize

postgres_service = PostgresService(
    name='name8',
    provider=CloudProvider.AWS,
    region='region4',
    postgres_version=PostgresMajorVersion.POSTGRES18,
    size=VmSize.Z3STANDARDLSSD88,
    id='f71df78e-ddad-82d0-8dfa-abbec741b82e',
    created_at=dateutil.parser.parse('2026-03-26T20:51:16.384Z'),
    is_primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

