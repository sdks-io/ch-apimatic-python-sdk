
# V1 Organizations Services Service Query Endpoint Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesServiceQueryEndpointResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ServiceQueryApiEndpoint`](../../doc/models/service-query-api-endpoint.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.role import Role
from openapispecforclickhousecloud.models.service_query_api_endpoint import ServiceQueryApiEndpoint
from openapispecforclickhousecloud.models.v_1_organizations_services_service_query_endpoint_response import V1OrganizationsServicesServiceQueryEndpointResponse

v_1_organizations_services_service_query_endpoint_response = V1OrganizationsServicesServiceQueryEndpointResponse(
    status=200,
    request_id='0000125e-0000-0000-0000-000000000000',
    result=ServiceQueryApiEndpoint(
        id='id6',
        open_api_keys=[
            'openApiKeys2'
        ],
        roles=[
            Role.SQL_CONSOLE_READ_ONLY,
            Role.SQL_CONSOLE_ADMIN,
            Role.SQL_CONSOLE_READ_ONLY
        ],
        allowed_origins='allowedOrigins2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

