
# Service Replica Scaling Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ServiceReplicaScalingPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min_replica_memory_gb` | `float` | Optional | Minimum auto-scaling memory in Gb for a single replica. Available only for 'production' services. Must be a multiple of 4 and greater than or equal to 8. A range in vertical autoscaling; equal to maxReplicaMemoryGb in horizontal.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `max_replica_memory_gb` | `float` | Optional | Maximum auto-scaling memory in Gb for a single replica. Available only for 'production' services. Must be a multiple of 4 and lower than or equal to 120 for non paid services or 356 for paid services. A range in vertical autoscaling; equal to minReplicaMemoryGb in horizontal.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `autoscaling_mode` | [`AutoscalingMode6`](../../doc/models/autoscaling-mode-6.md) | Optional | Target autoscaling mode. Omit to keep the service on its current mode. "vertical" runs a fixed replica count while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Switching to horizontal requires the feature to be enabled for the organization. |
| `num_replicas` | `int` | Optional | Fixed replica count for vertical autoscaling (autoscalingMode "vertical"). Mutually exclusive with minReplicas/maxReplicas. When switching to vertical (autoscalingMode "vertical") with numReplicas and no memory, the service's stored baseline per-replica memory is kept as the new vertical range. Please contact support to enable adjustment of numReplicas.<br><br>**Constraints**: `>= 1`, `<= 50` |
| `min_replicas` | `int` | Optional | Minimum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling (autoscalingMode "horizontal"). Must be provided together with maxReplicas. Mutually exclusive with numReplicas. Requires horizontal autoscaling to be enabled for the service, unless autoscalingMode is omitted or "vertical" and minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal entitlement).<br><br>**Constraints**: `>= 1`, `<= 50` |
| `max_replicas` | `int` | Optional | Maximum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling (autoscalingMode "horizontal"). Must be provided together with minReplicas. Mutually exclusive with numReplicas. Requires horizontal autoscaling to be enabled for the service, unless autoscalingMode is omitted or "vertical" and minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal entitlement).<br><br>**Constraints**: `>= 1`, `<= 50` |
| `idle_scaling` | `bool` | Optional | When set to true the service is allowed to scale down to zero when idle. True by default. |
| `idle_timeout_minutes` | `float` | Optional | Set minimum idling timeout (in minutes). Must be >= 5 minutes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_6 import AutoscalingMode6
from openapispecforclickhousecloud.models.service_replica_scaling_patch_request import ServiceReplicaScalingPatchRequest

service_replica_scaling_patch_request = ServiceReplicaScalingPatchRequest(
    min_replica_memory_gb=16,
    max_replica_memory_gb=120,
    autoscaling_mode=AutoscalingMode6.VERTICAL,
    num_replicas=3,
    min_replicas=1,
    max_replicas=5,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

