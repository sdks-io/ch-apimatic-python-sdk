
# V1 Organizations Services Clickpipes Reverse Private Endpoints Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[ReversePrivateEndpoint]`](../../doc/models/reverse-private-endpoint.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.reverse_private_endpoint import ReversePrivateEndpoint
from openapispecforclickhousecloud.models.type_1 import Type1
from openapispecforclickhousecloud.models.v_1_organizations_services_clickpipes_reverse_private_endpoints_response import V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse

v_1_organizations_services_clickpipes_reverse_private_endpoints_response = V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse(
    status=200,
    request_id='00001d9a-0000-0000-0000-000000000000',
    result=[
        ReversePrivateEndpoint(
            description='description6',
            mtype=Type1.MSK_MULTI_VPC,
            vpc_endpoint_service_name='vpcEndpointServiceName6',
            vpc_resource_configuration_id='vpcResourceConfigurationId8',
            vpc_resource_share_arn='vpcResourceShareArn6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ReversePrivateEndpoint(
            description='description6',
            mtype=Type1.MSK_MULTI_VPC,
            vpc_endpoint_service_name='vpcEndpointServiceName6',
            vpc_resource_configuration_id='vpcResourceConfigurationId8',
            vpc_resource_share_arn='vpcResourceShareArn6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

