
# V1 Organizations Services Replica Scaling Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesReplicaScalingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ServiceScalingPatchResponse`](../../doc/models/service-scaling-patch-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_3 import AutoscalingMode3
from openapispecforclickhousecloud.models.current_scaling import CurrentScaling
from openapispecforclickhousecloud.models.effective_autoscaling_mode import EffectiveAutoscalingMode
from openapispecforclickhousecloud.models.provider import Provider
from openapispecforclickhousecloud.models.region import Region
from openapispecforclickhousecloud.models.service_scaling_patch_response import ServiceScalingPatchResponse
from openapispecforclickhousecloud.models.state import State
from openapispecforclickhousecloud.models.v_1_organizations_services_replica_scaling_response import V1OrganizationsServicesReplicaScalingResponse

v_1_organizations_services_replica_scaling_response = V1OrganizationsServicesReplicaScalingResponse(
    status=200,
    request_id='00001146-0000-0000-0000-000000000000',
    result=ServiceScalingPatchResponse(
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
        id='000002b8-0000-0000-0000-000000000000',
        name='name6',
        provider=Provider.AZURE,
        region=Region.APSOUTHEAST2,
        state=State.PROVISIONING,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

