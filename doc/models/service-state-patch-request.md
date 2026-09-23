
# Service State Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ServiceStatePatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `command` | [`Command1`](../../doc/models/command-1.md) | Optional | Command to change the state: 'start', 'stop', 'awake'. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.command_1 import Command1
from openapispecforclickhousecloud.models.service_state_patch_request import ServiceStatePatchRequest

service_state_patch_request = ServiceStatePatchRequest(
    command=Command1.STOP,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

