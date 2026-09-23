
# V1 Organizations Services Scaling Schedule Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesScalingScheduleResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ScalingSchedule`](../../doc/models/scaling-schedule.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode import AutoscalingMode
from openapispecforclickhousecloud.models.autoscaling_mode_1 import AutoscalingMode1
from openapispecforclickhousecloud.models.scaling_schedule import ScalingSchedule
from openapispecforclickhousecloud.models.scaling_schedule_base_config import ScalingScheduleBaseConfig
from openapispecforclickhousecloud.models.scaling_schedule_entry import ScalingScheduleEntry
from openapispecforclickhousecloud.models.v_1_organizations_services_scaling_schedule_response import V1OrganizationsServicesScalingScheduleResponse

v_1_organizations_services_scaling_schedule_response = V1OrganizationsServicesScalingScheduleResponse(
    status=200,
    request_id='000018b0-0000-0000-0000-000000000000',
    result=ScalingSchedule(
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
            ),
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
            ),
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
        active_entry_id='00000204-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

