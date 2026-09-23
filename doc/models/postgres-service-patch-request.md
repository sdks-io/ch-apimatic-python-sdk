
# Postgres Service Patch Request

*This model accepts additional fields of type Any.*

## Structure

`PostgresServicePatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `size` | [`VmSize`](../../doc/models/vm-size.md) | Optional | The VM size for a Postgres service. |
| `ha_type` | [`PgHaType`](../../doc/models/pg-ha-type.md) | Optional | Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby, and “sync” for synchronous replication to two standbys. |
| `tags` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use.<br><br>**Constraints**: *Maximum Items*: `50` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.pg_ha_type import PgHaType
from openapispecforclickhousecloud.models.postgres_service_patch_request import PostgresServicePatchRequest
from openapispecforclickhousecloud.models.resource_tags_v_1 import ResourceTagsV1
from openapispecforclickhousecloud.models.vm_size import VmSize

postgres_service_patch_request = PostgresServicePatchRequest(
    name='name2',
    size=VmSize.ENUM_R6ID16XLARGE,
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

