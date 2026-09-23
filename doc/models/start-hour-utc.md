
# Start Hour Utc

UTC hour when the upgrade window starts. Must be one of 0, 6, 12, or 18.

## Enumeration

`StartHourUtc`

## Fields

| Name | Description |
|  --- | --- |
| `HOUR0` | Upgrade window starts at 00:00 UTC. |
| `HOUR6` | Upgrade window starts at 06:00 UTC. |
| `HOUR12` | Upgrade window starts at 12:00 UTC. |
| `HOUR18` | Upgrade window starts at 18:00 UTC. |

## Example

```python
from openapispecforclickhousecloud.models.start_hour_utc import StartHourUtc

start_hour_utc = StartHourUtc.HOUR12
```

