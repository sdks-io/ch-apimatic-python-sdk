
# V1 Organizations Services Private Endpoint Config Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesPrivateEndpointConfigResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`PrivateEndpointConfig`](../../doc/models/private-endpoint-config.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.private_endpoint_config import PrivateEndpointConfig
from openapispecforclickhousecloud.models.v_1_organizations_services_private_endpoint_config_response import V1OrganizationsServicesPrivateEndpointConfigResponse

v_1_organizations_services_private_endpoint_config_response = V1OrganizationsServicesPrivateEndpointConfigResponse(
    status=200,
    request_id='000022f6-0000-0000-0000-000000000000',
    result=PrivateEndpointConfig(
        endpoint_service_id='endpointServiceId4',
        private_dns_hostname='privateDnsHostname2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

