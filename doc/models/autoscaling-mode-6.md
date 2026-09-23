
# Autoscaling Mode 6

Target autoscaling mode. Omit to keep the service on its current mode. "vertical" runs a fixed replica count while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Switching to horizontal requires the feature to be enabled for the organization.

## Enumeration

`AutoscalingMode6`

## Fields

| Name |
|  --- |
| `VERTICAL` |
| `HORIZONTAL` |

## Example

```python
from openapispecforclickhousecloud.models.autoscaling_mode_6 import AutoscalingMode6

autoscaling_mode_6 = AutoscalingMode6.VERTICAL
```

