
# V1 Organizations Services Clickpipes Context Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesContextResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickPipesServiceContext`](../../doc/models/click-pipes-service-context.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipes_gcp_workload_identity_context import ClickPipesGcpWorkloadIdentityContext
from openapispecforclickhousecloud.models.click_pipes_service_context import ClickPipesServiceContext
from openapispecforclickhousecloud.models.v_1_organizations_services_clickpipes_context_response import V1OrganizationsServicesClickpipesContextResponse

v_1_organizations_services_clickpipes_context_response = V1OrganizationsServicesClickpipesContextResponse(
    status=200,
    request_id='00001d7c-0000-0000-0000-000000000000',
    result=ClickPipesServiceContext(
        gcp_workload_identity=ClickPipesGcpWorkloadIdentityContext(
            supported=False,
            ready=False,
            principal='principal0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

