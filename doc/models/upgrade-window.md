
# Upgrade Window

*This model accepts additional fields of type Any.*

## Structure

`UpgradeWindow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `weekday` | `int` | Required | Day of the week the upgrade window starts. 0 = Sunday, 1 = Monday, …, 6 = Saturday.<br><br>**Constraints**: `>= 0`, `<= 6` |
| `start_hour_utc` | [`StartHourUtc`](../../doc/models/start-hour-utc.md) | Required | UTC hour when the upgrade window starts. Must be one of 0, 6, 12, or 18. |
| `duration` | `int` | Required, Constant | Length of the upgrade window in hours. Currently only a 6-hour window is supported.<br><br>**Value**: `6` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.start_hour_utc import StartHourUtc
from openapispecforclickhousecloud.models.upgrade_window import UpgradeWindow

upgrade_window = UpgradeWindow(
    weekday=3,
    start_hour_utc=StartHourUtc.HOUR12,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

