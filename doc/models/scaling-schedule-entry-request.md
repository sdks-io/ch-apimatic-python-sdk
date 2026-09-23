
# Scaling Schedule Entry Request

*This model accepts additional fields of type Any.*

## Structure

`ScalingScheduleEntryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Human-readable label for this schedule entry. |
| `weekdays` | `List[int]` | Required | Days of the week this entry applies to. 0 = Sunday, 1 = Monday, …, 6 = Saturday.<br><br>**Constraints**: *Minimum Items*: `1` |
| `start_hour_utc` | `int` | Required | UTC hour (0–23) when this entry becomes active (inclusive).<br><br>**Constraints**: `>= 0`, `<= 23` |
| `end_hour_utc` | `int` | Required | UTC hour (1–24) when this entry deactivates (exclusive). Must differ from startHourUtc. Set to 24 to end at midnight. Values less than startHourUtc create an overnight window spanning midnight.<br><br>**Constraints**: `>= 1`, `<= 24` |
| `autoscaling_mode` | [`AutoscalingMode2`](../../doc/models/autoscaling-mode-2.md) | Optional | Autoscaling mode for this entry. "vertical" (the default when omitted) runs a fixed replica count while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Horizontal requires the feature to be enabled for the organization. |
| `min_replica_memory_gb` | `float` | Optional | Minimum memory per replica (Gb). Optional for vertical entries — provide both bounds for a memory range, or omit both to inherit memory from the base scaling config. Required for horizontal (both bounds, equal to maxReplicaMemoryGb — memory is fixed while the replica count scales). The upper bound is tier-dependent (lower for non-paid organizations) and enforced when the entry is applied.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `max_replica_memory_gb` | `float` | Optional | Maximum memory per replica (Gb). Optional for vertical entries — provide both bounds for a memory range, or omit both to inherit memory from the base scaling config. Required for horizontal (both bounds, equal to minReplicaMemoryGb — memory is fixed while the replica count scales). The upper bound is tier-dependent (lower for non-paid organizations) and enforced when the entry is applied.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `num_replicas` | `int` | Optional | Fixed replica count for a vertical entry (autoscalingMode "vertical" or omitted). Mutually exclusive with minReplicas/maxReplicas. The per-service replica maximum is variable (tier-dependent, configurable per service) and enforced when the entry is applied, not at request time.<br><br>**Constraints**: `>= 1` |
| `min_replicas` | `int` | Optional | Minimum number of replicas. A minReplicas/maxReplicas band scales the replica count in a horizontal entry (autoscalingMode "horizontal"); when autoscalingMode is omitted or "vertical", an equal band (minReplicas === maxReplicas) is instead an accepted vertical fixed count and needs no horizontal entitlement. Must be provided together with maxReplicas. The per-service replica maximum is variable (tier-dependent, configurable per service) and enforced when the entry is applied, not at request time.<br><br>**Constraints**: `>= 1` |
| `max_replicas` | `int` | Optional | Maximum number of replicas. A minReplicas/maxReplicas band scales the replica count in a horizontal entry (autoscalingMode "horizontal"); when autoscalingMode is omitted or "vertical", an equal band (minReplicas === maxReplicas) is instead an accepted vertical fixed count and needs no horizontal entitlement. Must be provided together with minReplicas. The per-service replica maximum is variable (tier-dependent, configurable per service) and enforced when the entry is applied, not at request time.<br><br>**Constraints**: `>= 1` |
| `idle_scaling` | `bool` | Optional | Whether idle scaling is enabled during this window. |
| `idle_timeout_minutes` | `int` | Optional | Idle timeout in minutes during this window. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_2 import AutoscalingMode2
from openapispecforclickhousecloud.models.scaling_schedule_entry_request import ScalingScheduleEntryRequest

scaling_schedule_entry_request = ScalingScheduleEntryRequest(
    name='Business hours',
    weekdays=[
        1,
        2,
        3,
        4,
        5
    ],
    start_hour_utc=9,
    end_hour_utc=17,
    autoscaling_mode=AutoscalingMode2.VERTICAL,
    min_replica_memory_gb=16,
    max_replica_memory_gb=16,
    num_replicas=3,
    min_replicas=2,
    max_replicas=3,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

