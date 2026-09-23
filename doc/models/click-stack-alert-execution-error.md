
# Click Stack Alert Execution Error

*This model accepts additional fields of type Any.*

## Structure

`ClickStackAlertExecutionError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `datetime` | Required | When the error occurred. |
| `mtype` | [`Type15`](../../doc/models/type-15.md) | Required | Category of the error. |
| `message` | `str` | Required | Human-readable error message. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_alert_execution_error import ClickStackAlertExecutionError
from openapispecforclickhousecloud.models.type_15 import Type15

click_stack_alert_execution_error = ClickStackAlertExecutionError(
    timestamp=dateutil.parser.parse('2026-04-17T12:00:00Z'),
    mtype=Type15.QUERY_ERROR,
    message='Query timed out after 30s',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

