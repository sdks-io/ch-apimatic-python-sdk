
# Scaling Schedule

*This model accepts additional fields of type Any.*

## Structure

`ScalingSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entries` | [`List[ScalingScheduleEntry]`](../../doc/models/scaling-schedule-entry.md) | Required | List of schedule entries. |
| `base_config` | [`ScalingScheduleBaseConfig`](../../doc/models/scaling-schedule-base-config.md) | Required | - |
| `active_entry_id` | `uuid\|str` | Optional | ID of the currently-active schedule entry. Absent when no entry is active and the base config is in effect. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode import AutoscalingMode
from openapispecforclickhousecloud.models.autoscaling_mode_1 import AutoscalingMode1
from openapispecforclickhousecloud.models.scaling_schedule import ScalingSchedule
from openapispecforclickhousecloud.models.scaling_schedule_base_config import ScalingScheduleBaseConfig
from openapispecforclickhousecloud.models.scaling_schedule_entry import ScalingScheduleEntry

scaling_schedule = ScalingSchedule(
    entries=[
        ScalingScheduleEntry(
            id='00000582-0000-0000-0000-000000000000',
            name='name0',
            weekdays=[
                212
            ],
            start_hour_utc=23,
            end_hour_utc=24,
            autoscaling_mode=AutoscalingMode.VERTICAL,
            is_active_now=False,
            min_replica_memory_gb=252.2,
            max_replica_memory_gb=53.64,
            min_replicas=232,
            max_replicas=106,
            idle_scaling=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    base_config=ScalingScheduleBaseConfig(
        autoscaling_mode=AutoscalingMode1.VERTICAL,
        min_replica_memory_gb=68.3,
        max_replica_memory_gb=237.54,
        min_replicas=18,
        max_replicas=148,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    active_entry_id='000011e6-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

