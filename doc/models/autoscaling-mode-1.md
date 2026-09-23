
# Autoscaling Mode 1

Autoscaling mode applied when no schedule entry is active. "vertical" runs a fixed replica count while memory scales; "horizontal" scales the replica count at a fixed per-replica memory.

## Enumeration

`AutoscalingMode1`

## Fields

| Name |
|  --- |
| `VERTICAL` |
| `HORIZONTAL` |

## Example

```python
from openapispecforclickhousecloud.models.autoscaling_mode_1 import AutoscalingMode1

autoscaling_mode_1 = AutoscalingMode1.VERTICAL
```

