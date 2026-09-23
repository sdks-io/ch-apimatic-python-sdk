
# Service Query Api Endpoint

*This model accepts additional fields of type Any.*

## Structure

`ServiceQueryApiEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The id of the service query endpoint |
| `open_api_keys` | `List[str]` | Optional | List of OpenAPI keys that can access the service query endpoint |
| `roles` | [`List[Role]`](../../doc/models/role.md) | Optional | List of roles that can access the service query endpoint |
| `allowed_origins` | `str` | Optional | The allowed origins as comma separated list of domains |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.role import Role
from openapispecforclickhousecloud.models.service_query_api_endpoint import ServiceQueryApiEndpoint

service_query_api_endpoint = ServiceQueryApiEndpoint(
    id='id8',
    open_api_keys=[
        'openApiKeys4'
    ],
    roles=[
        Role.SQL_CONSOLE_READ_ONLY,
        Role.SQL_CONSOLE_ADMIN,
        Role.SQL_CONSOLE_READ_ONLY
    ],
    allowed_origins='allowedOrigins4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

