
# V1 Organizations Services Clickpipes Reverse Private Endpoints Reverse Private Endpoint Id Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.v_1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response_1 import V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1

v_1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response_1 = V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1(
    status=200,
    request_id='00000794-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

