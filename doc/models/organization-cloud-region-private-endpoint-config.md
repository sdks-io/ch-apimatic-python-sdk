
# Organization Cloud Region Private Endpoint Config

*This model accepts additional fields of type Any.*

## Structure

`OrganizationCloudRegionPrivateEndpointConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `endpoint_service_id` | `str` | Optional | Unique identifier of the interface endpoint you created in your VPC with the AWS(Service Name) or GCP(Target Service) resource |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.organization_cloud_region_private_endpoint_config import OrganizationCloudRegionPrivateEndpointConfig

organization_cloud_region_private_endpoint_config = OrganizationCloudRegionPrivateEndpointConfig(
    endpoint_service_id='endpointServiceId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

