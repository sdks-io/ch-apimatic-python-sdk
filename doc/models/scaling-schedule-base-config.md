
# Scaling Schedule Base Config

*This model accepts additional fields of type Any.*

## Structure

`ScalingScheduleBaseConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `autoscaling_mode` | [`AutoscalingMode1`](../../doc/models/autoscaling-mode-1.md) | Optional | Autoscaling mode applied when no schedule entry is active. "vertical" runs a fixed replica count while memory scales; "horizontal" scales the replica count at a fixed per-replica memory. |
| `min_replica_memory_gb` | `float` | Optional | Minimum memory per replica (Gb) when no schedule entry is active. Absent for services that do not autoscale memory. |
| `max_replica_memory_gb` | `float` | Optional | Maximum memory per replica (Gb) when no schedule entry is active. Absent for services that do not autoscale memory. |
| `min_replicas` | `int` | Optional | Minimum number of replicas when no schedule entry is active. |
| `max_replicas` | `int` | Optional | Maximum number of replicas when no schedule entry is active. |
| `idle_scaling` | `bool` | Optional | Whether idle scaling is enabled when no schedule entry is active. |
| `idle_timeout_minutes` | `int` | Optional | Idle timeout in minutes when no schedule entry is active. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_1 import AutoscalingMode1
from openapispecforclickhousecloud.models.scaling_schedule_base_config import ScalingScheduleBaseConfig

scaling_schedule_base_config = ScalingScheduleBaseConfig(
    autoscaling_mode=AutoscalingMode1.VERTICAL,
    min_replica_memory_gb=40.12,
    max_replica_memory_gb=9.72,
    min_replicas=16,
    max_replicas=146,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

