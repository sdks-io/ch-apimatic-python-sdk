
# Private Endpoint Config

*This model accepts additional fields of type Any.*

## Structure

`PrivateEndpointConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `endpoint_service_id` | `str` | Optional | Unique identifier of the interface endpoint you created in your VPC with the AWS(Service Name), GCP(Target Service) or AZURE (Private Link Service) resource |
| `private_dns_hostname` | `str` | Optional | Private DNS Hostname of the VPC you created |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.private_endpoint_config import PrivateEndpointConfig

private_endpoint_config = PrivateEndpointConfig(
    endpoint_service_id='endpointServiceId0',
    private_dns_hostname='privateDnsHostname4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

