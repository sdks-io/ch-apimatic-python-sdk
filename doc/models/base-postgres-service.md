
# Base Postgres Service

*This model accepts additional fields of type Any.*

## Structure

`BasePostgresService`

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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.base_postgres_service import BasePostgresService
from openapispecforclickhousecloud.models.cloud_provider import CloudProvider
from openapispecforclickhousecloud.models.postgres_major_version import PostgresMajorVersion
from openapispecforclickhousecloud.models.vm_size import VmSize

base_postgres_service = BasePostgresService(
    name='name6',
    provider=CloudProvider.AWS,
    region='region2',
    postgres_version=PostgresMajorVersion.POSTGRES18,
    size=VmSize.Z3HIGHLSSD16,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

