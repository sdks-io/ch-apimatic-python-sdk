
# Autoscaling Mode

Autoscaling mode for this entry. "vertical" runs a fixed replica count while memory scales; "horizontal" scales the replica count at a fixed per-replica memory. Defaults to "vertical" for entries persisted before the mode was exposed.

## Enumeration

`AutoscalingMode`

## Fields

| Name |
|  --- |
| `VERTICAL` |
| `HORIZONTAL` |

## Example

```python
from openapispecforclickhousecloud.models.autoscaling_mode import AutoscalingMode

autoscaling_mode = AutoscalingMode.VERTICAL
```

