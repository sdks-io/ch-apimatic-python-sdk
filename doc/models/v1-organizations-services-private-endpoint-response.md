
# V1 Organizations Services Private Endpoint Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesPrivateEndpointResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`InstancePrivateEndpoint`](../../doc/models/instance-private-endpoint.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider_1 import CloudProvider1
from openapispecforclickhousecloud.models.instance_private_endpoint import InstancePrivateEndpoint
from openapispecforclickhousecloud.models.region_1 import Region1
from openapispecforclickhousecloud.models.v_1_organizations_services_private_endpoint_response import V1OrganizationsServicesPrivateEndpointResponse

v_1_organizations_services_private_endpoint_response = V1OrganizationsServicesPrivateEndpointResponse(
    status=200,
    request_id='00000c52-0000-0000-0000-000000000000',
    result=InstancePrivateEndpoint(
        id='id6',
        description='description6',
        cloud_provider=CloudProvider1.AZURE,
        region=Region1.APSOUTHEAST2,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

