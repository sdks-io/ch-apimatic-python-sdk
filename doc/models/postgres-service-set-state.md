
# Postgres Service Set State

*This model accepts additional fields of type Any.*

## Structure

`PostgresServiceSetState`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `command` | [`Command`](../../doc/models/command.md) | Optional | Postgres status, which initiates a process. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.command import Command
from openapispecforclickhousecloud.models.postgres_service_set_state import PostgresServiceSetState

postgres_service_set_state = PostgresServiceSetState(
    command=Command.RESTART,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

