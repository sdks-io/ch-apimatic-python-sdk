
# V1 Organizations Postgres State Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresStateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`PostgresService`](../../doc/models/postgres-service.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider import CloudProvider
from openapispecforclickhousecloud.models.postgres_major_version import PostgresMajorVersion
from openapispecforclickhousecloud.models.postgres_service import PostgresService
from openapispecforclickhousecloud.models.v_1_organizations_postgres_state_response import V1OrganizationsPostgresStateResponse
from openapispecforclickhousecloud.models.vm_size import VmSize

v_1_organizations_postgres_state_response = V1OrganizationsPostgresStateResponse(
    status=200,
    request_id='00000996-0000-0000-0000-000000000000',
    result=PostgresService(
        name='name6',
        provider=CloudProvider.AWS,
        region='region2',
        postgres_version=PostgresMajorVersion.POSTGRES18,
        size=VmSize.ENUM_I7IE6XLARGE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

