
# Autoscaling Mode 4

Autoscaling mode. "vertical" (the default when omitted) runs a fixed replica count while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Horizontal requires the feature to be enabled for the organization.

## Enumeration

`AutoscalingMode4`

## Fields

| Name |
|  --- |
| `VERTICAL` |
| `HORIZONTAL` |

## Example

```python
from openapispecforclickhousecloud.models.autoscaling_mode_4 import AutoscalingMode4

autoscaling_mode_4 = AutoscalingMode4.VERTICAL
```

