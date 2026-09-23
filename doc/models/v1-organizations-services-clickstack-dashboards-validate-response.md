
# V1 Organizations Services Clickstack Dashboards Validate Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackDashboardsValidateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickStackValidateDashboardResponse`](../../doc/models/click-stack-validate-dashboard-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_validate_dashboard_error import ClickStackValidateDashboardError
from openapispecforclickhousecloud.models.click_stack_validate_dashboard_response import ClickStackValidateDashboardResponse
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_dashboards_validate_response import V1OrganizationsServicesClickstackDashboardsValidateResponse

v_1_organizations_services_clickstack_dashboards_validate_response = V1OrganizationsServicesClickstackDashboardsValidateResponse(
    status=200,
    request_id='00000cf0-0000-0000-0000-000000000000',
    result=ClickStackValidateDashboardResponse(
        valid=False,
        errors=[
            ClickStackValidateDashboardError(
                path='path4',
                message='message0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ClickStackValidateDashboardError(
                path='path4',
                message='message0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        normalized=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

