
# Effective Autoscaling Mode

Autoscaling mode currently in effect on the running service. May diverge from the configured baseline mode while a schedule entry is active.

## Enumeration

`EffectiveAutoscalingMode`

## Fields

| Name |
|  --- |
| `VERTICAL` |
| `HORIZONTAL` |

## Example

```python
from openapispecforclickhousecloud.models.effective_autoscaling_mode import EffectiveAutoscalingMode

effective_autoscaling_mode = EffectiveAutoscalingMode.VERTICAL
```

