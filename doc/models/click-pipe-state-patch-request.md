
# Click Pipe State Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeStatePatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `command` | [`Command2`](../../doc/models/command-2.md) | Optional | Command to change the state: 'start', 'stop', 'resync'. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_state_patch_request import ClickPipeStatePatchRequest
from openapispecforclickhousecloud.models.command_2 import Command2

click_pipe_state_patch_request = ClickPipeStatePatchRequest(
    command=Command2.STOP,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

