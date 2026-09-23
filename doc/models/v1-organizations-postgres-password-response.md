
# V1 Organizations Postgres Password Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresPasswordResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`PostgresServicePasswordResource`](../../doc/models/postgres-service-password-resource.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_service_password_resource import PostgresServicePasswordResource
from openapispecforclickhousecloud.models.v_1_organizations_postgres_password_response import V1OrganizationsPostgresPasswordResponse

v_1_organizations_postgres_password_response = V1OrganizationsPostgresPasswordResponse(
    status=200,
    request_id='0000230c-0000-0000-0000-000000000000',
    result=PostgresServicePasswordResource(
        password='password0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

