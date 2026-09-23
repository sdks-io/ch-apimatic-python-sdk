
# V1 Organizations Services Upgrade Window Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesUpgradeWindowResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`UpgradeWindow`](../../doc/models/upgrade-window.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.start_hour_utc import StartHourUtc
from openapispecforclickhousecloud.models.upgrade_window import UpgradeWindow
from openapispecforclickhousecloud.models.v_1_organizations_services_upgrade_window_response import V1OrganizationsServicesUpgradeWindowResponse

v_1_organizations_services_upgrade_window_response = V1OrganizationsServicesUpgradeWindowResponse(
    status=200,
    request_id='000007b2-0000-0000-0000-000000000000',
    result=UpgradeWindow(
        weekday=6,
        start_hour_utc=StartHourUtc.HOUR0,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

