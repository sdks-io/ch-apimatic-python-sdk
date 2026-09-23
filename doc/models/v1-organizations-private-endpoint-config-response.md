
# V1 Organizations Private Endpoint Config Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPrivateEndpointConfigResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`OrganizationCloudRegionPrivateEndpointConfig`](../../doc/models/organization-cloud-region-private-endpoint-config.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.organization_cloud_region_private_endpoint_config import OrganizationCloudRegionPrivateEndpointConfig
from openapispecforclickhousecloud.models.v_1_organizations_private_endpoint_config_response import V1OrganizationsPrivateEndpointConfigResponse

v_1_organizations_private_endpoint_config_response = V1OrganizationsPrivateEndpointConfigResponse(
    status=200,
    request_id='000012b4-0000-0000-0000-000000000000',
    result=OrganizationCloudRegionPrivateEndpointConfig(
        endpoint_service_id='endpointServiceId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

