
# Current Scaling

*This model accepts additional fields of type Any.*

## Structure

`CurrentScaling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `effective_autoscaling_mode` | [`EffectiveAutoscalingMode`](../../doc/models/effective-autoscaling-mode.md) | Optional | Autoscaling mode currently in effect on the running service. May diverge from the configured baseline mode while a schedule entry is active. |
| `effective_min_replica_memory_gb` | `float` | Optional | Minimum memory per replica (Gb) currently applied to the running service. May diverge from the top-level `minReplicaMemoryGb` baseline while a schedule entry is active. |
| `effective_max_replica_memory_gb` | `float` | Optional | Maximum memory per replica (Gb) currently applied to the running service. May diverge from the top-level `maxReplicaMemoryGb` baseline while a schedule entry is active. Reflects the stored value: normally equal to `effectiveMinReplicaMemoryGb` in horizontal mode, but a legacy service stored with an unequal memory range reports the stored bounds as-is. |
| `effective_min_replicas` | `int` | Optional | Minimum number of replicas currently applied to the running service. May diverge from the baseline while a schedule entry is active. Reflects the stored value: normally equal to `effectiveMaxReplicas` in vertical mode (a fixed replica count), but a legacy service stored with an unequal replica range reports the stored bounds as-is. |
| `effective_max_replicas` | `int` | Optional | Maximum number of replicas currently applied to the running service. May diverge from the baseline while a schedule entry is active. |
| `effective_idle_scaling` | `bool` | Optional | Whether idle scaling is currently in effect on the service. May diverge from the top-level `idleScaling` baseline while a schedule entry is active. |
| `effective_idle_timeout_minutes` | `int` | Optional | Idle timeout in minutes currently in effect on the service. May diverge from the top-level `idleTimeoutMinutes` baseline while a schedule entry is active. |
| `active_entry_id` | `uuid\|str` | Optional | ID of the schedule entry whose values are currently applied to the service. Absent when no entry is active. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.current_scaling import CurrentScaling
from openapispecforclickhousecloud.models.effective_autoscaling_mode import EffectiveAutoscalingMode

current_scaling = CurrentScaling(
    effective_autoscaling_mode=EffectiveAutoscalingMode.VERTICAL,
    effective_min_replica_memory_gb=62.38,
    effective_max_replica_memory_gb=2.1,
    effective_min_replicas=110,
    effective_max_replicas=26,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

