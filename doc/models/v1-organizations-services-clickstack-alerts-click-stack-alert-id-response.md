
# V1 Organizations Services Clickstack Alerts Click Stack Alert Id Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickStackAlertResponse`](../../doc/models/click-stack-alert-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_alert_response import ClickStackAlertResponse
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_alerts_click_stack_alert_id_response import V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse

v_1_organizations_services_clickstack_alerts_click_stack_alert_id_response = V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse(
    status=200,
    request_id='00000fb2-0000-0000-0000-000000000000',
    result=ClickStackAlertResponse(
        dashboard_id='dashboardId6',
        tile_id='tileId2',
        saved_search_id='savedSearchId6',
        group_by='groupBy4',
        threshold=139.44,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

