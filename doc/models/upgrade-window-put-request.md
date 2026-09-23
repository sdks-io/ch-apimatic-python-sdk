
# Upgrade Window Put Request

*This model accepts additional fields of type Any.*

## Structure

`UpgradeWindowPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `weekday` | `int` | Required | Day of the week the upgrade window starts. 0 = Sunday, 1 = Monday, …, 6 = Saturday.<br><br>**Constraints**: `>= 0`, `<= 6` |
| `start_hour_utc` | [`StartHourUtc1`](../../doc/models/start-hour-utc-1.md) | Required | UTC hour when the upgrade window starts. Must be one of 0, 6, 12, or 18. The upgrade window currently lasts 6 hours from this start time. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.start_hour_utc_1 import StartHourUtc1
from openapispecforclickhousecloud.models.upgrade_window_put_request import UpgradeWindowPutRequest

upgrade_window_put_request = UpgradeWindowPutRequest(
    weekday=3,
    start_hour_utc=StartHourUtc1.HOUR12,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

