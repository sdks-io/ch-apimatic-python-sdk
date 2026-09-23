
# Service Post Response

*This model accepts additional fields of type Any.*

## Structure

`ServicePostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service` | [`Service`](../../doc/models/service.md) | Optional | - |
| `password` | `str` | Optional | Password for the newly created service. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_3 import AutoscalingMode3
from openapispecforclickhousecloud.models.current_scaling import CurrentScaling
from openapispecforclickhousecloud.models.effective_autoscaling_mode import EffectiveAutoscalingMode
from openapispecforclickhousecloud.models.provider import Provider
from openapispecforclickhousecloud.models.region import Region
from openapispecforclickhousecloud.models.service import Service
from openapispecforclickhousecloud.models.service_post_response import ServicePostResponse
from openapispecforclickhousecloud.models.state import State

service_post_response = ServicePostResponse(
    service=Service(
        autoscaling_mode=AutoscalingMode3.VERTICAL,
        current_scaling=CurrentScaling(
            effective_autoscaling_mode=EffectiveAutoscalingMode.VERTICAL,
            effective_min_replica_memory_gb=39.2,
            effective_max_replica_memory_gb=21.08,
            effective_min_replicas=124,
            effective_max_replicas=40,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        id='000023dc-0000-0000-0000-000000000000',
        name='name0',
        provider=Provider.AWS,
        region=Region.APNORTHEAST1,
        state=State.TERMINATING,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    password='password6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

