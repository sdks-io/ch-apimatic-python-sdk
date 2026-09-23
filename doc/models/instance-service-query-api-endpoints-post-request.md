
# Instance Service Query Api Endpoints Post Request

*This model accepts additional fields of type Any.*

## Structure

`InstanceServiceQueryApiEndpointsPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `roles` | [`List[Role]`](../../doc/models/role.md) | Optional | The roles |
| `open_api_keys` | `List[str]` | Optional | The version of the service query endpoint |
| `allowed_origins` | `str` | Optional | The allowed origins as comma separated list of domains |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.instance_service_query_api_endpoints_post_request import InstanceServiceQueryApiEndpointsPostRequest
from openapispecforclickhousecloud.models.role import Role

instance_service_query_api_endpoints_post_request = InstanceServiceQueryApiEndpointsPostRequest(
    roles=[
        Role.SQL_CONSOLE_READ_ONLY,
        Role.SQL_CONSOLE_ADMIN
    ],
    open_api_keys=[
        'openApiKeys6',
        'openApiKeys7'
    ],
    allowed_origins='allowedOrigins4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

