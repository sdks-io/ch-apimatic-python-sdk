
# Scaling Schedule Post Request

*This model accepts additional fields of type Any.*

## Structure

`ScalingSchedulePostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entries` | [`List[ScalingScheduleEntryRequest]`](../../doc/models/scaling-schedule-entry-request.md) | Required | List of schedule entries. Pass an empty array to clear the schedule. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_2 import AutoscalingMode2
from openapispecforclickhousecloud.models.scaling_schedule_entry_request import ScalingScheduleEntryRequest
from openapispecforclickhousecloud.models.scaling_schedule_post_request import ScalingSchedulePostRequest

scaling_schedule_post_request = ScalingSchedulePostRequest(
    entries=[
        ScalingScheduleEntryRequest(
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

