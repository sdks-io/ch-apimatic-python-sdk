
# Click Stack Alert Silenced

*This model accepts additional fields of type Any.*

## Structure

`ClickStackAlertSilenced`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `by` | `str` | Optional | User ID who silenced the alert. |
| `at` | `datetime` | Optional | Silence start timestamp. |
| `until` | `datetime` | Optional | Silence end timestamp. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_alert_silenced import ClickStackAlertSilenced

click_stack_alert_silenced = ClickStackAlertSilenced(
    by='65f5e4a3b9e77c001a234567',
    at=dateutil.parser.parse('2026-03-19T08:00:00Z'),
    until=dateutil.parser.parse('2026-03-20T08:00:00Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

