
# Service State

Current state of the service.

## Enumeration

`ServiceState`

## Fields

| Name |
|  --- |
| `STARTING` |
| `STOPPING` |
| `TERMINATING` |
| `SOFTDELETING` |
| `AWAKING` |
| `PARTIALLY_RUNNING` |
| `PROVISIONING` |
| `RUNNING` |
| `STOPPED` |
| `TERMINATED` |
| `SOFTDELETED` |
| `DEGRADED` |
| `FAILED` |
| `IDLE` |

## Example

```python
from openapispecforclickhousecloud.models.service_state import ServiceState

service_state = ServiceState.AWAKING
```

