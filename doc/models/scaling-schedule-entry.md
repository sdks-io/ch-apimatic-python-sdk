
# Scaling Schedule Entry

*This model accepts additional fields of type Any.*

## Structure

`ScalingScheduleEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique identifier for this schedule entry. |
| `name` | `str` | Required | Human-readable label for this schedule entry. |
| `weekdays` | `List[int]` | Required | Days of the week this entry applies to. 0 = Sunday, 1 = Monday, …, 6 = Saturday.<br><br>**Constraints**: *Minimum Items*: `1` |
| `start_hour_utc` | `int` | Required | UTC hour (0–23) when this entry becomes active (inclusive).<br><br>**Constraints**: `>= 0`, `<= 23` |
| `end_hour_utc` | `int` | Required | UTC hour (1–24) when this entry deactivates (exclusive). Must differ from startHourUtc. Set to 24 to end at midnight. Values less than startHourUtc create an overnight window spanning midnight.<br><br>**Constraints**: `>= 1`, `<= 24` |
| `autoscaling_mode` | [`AutoscalingMode`](../../doc/models/autoscaling-mode.md) | Required | Autoscaling mode for this entry. "vertical" runs a fixed replica count while memory scales; "horizontal" scales the replica count at a fixed per-replica memory. Defaults to "vertical" for entries persisted before the mode was exposed. |
| `min_replica_memory_gb` | `float` | Optional | Minimum memory per replica (Gb) during this window. A range in vertical; in horizontal it equals maxReplicaMemoryGb (memory is fixed while the replica count scales). |
| `max_replica_memory_gb` | `float` | Optional | Maximum memory per replica (Gb) during this window. A range in vertical; in horizontal it equals minReplicaMemoryGb (memory is fixed while the replica count scales). |
| `min_replicas` | `int` | Optional | Minimum number of replicas during this window. For a horizontal entry the replica count scales between minReplicas and maxReplicas; for a vertical entry minReplicas and maxReplicas are equal and report the fixed replica count (both omitted when the entry stored no count). |
| `max_replicas` | `int` | Optional | Maximum number of replicas during this window. For a horizontal entry the replica count scales between minReplicas and maxReplicas; for a vertical entry minReplicas and maxReplicas are equal and report the fixed replica count (both omitted when the entry stored no count). |
| `idle_scaling` | `bool` | Optional | Whether idle scaling is enabled during this window. |
| `idle_timeout_minutes` | `int` | Optional | Idle timeout in minutes during this window. |
| `is_active_now` | `bool` | Required | Whether this entry is currently active. Scheduled times are indicative — actions are applied on a best-effort basis and may be delayed by a few minutes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode import AutoscalingMode
from openapispecforclickhousecloud.models.scaling_schedule_entry import ScalingScheduleEntry

scaling_schedule_entry = ScalingScheduleEntry(
    id='00001882-0000-0000-0000-000000000000',
    name='name4',
    weekdays=[
        212,
        211,
        210
    ],
    start_hour_utc=23,
    end_hour_utc=24,
    autoscaling_mode=AutoscalingMode.VERTICAL,
    is_active_now=False,
    min_replica_memory_gb=44.84,
    max_replica_memory_gb=5,
    min_replicas=232,
    max_replicas=106,
    idle_scaling=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

