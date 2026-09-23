
# Click Stack Generic Webhook

*This model accepts additional fields of type Any.*

## Structure

`ClickStackGenericWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Webhook ID |
| `name` | `str` | Required | Webhook name |
| `service` | `str` | Required, Constant | Webhook service type<br><br>**Value**: `"generic"` |
| `url` | `str` | Optional | Webhook destination URL |
| `description` | `str` | Optional | Webhook description, shown in the UI |
| `body` | `str` | Optional | Optional request body template |
| `updated_at` | `datetime` | Required | Last update timestamp |
| `created_at` | `datetime` | Required | Creation timestamp |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_generic_webhook import ClickStackGenericWebhook

click_stack_generic_webhook = ClickStackGenericWebhook(
    id='507f1f77bcf86cd799439013',
    name='PagerDuty Integration',
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://example.com/webhooks/alerts',
    description='Forwards alert payloads to an external monitoring service',
    body='{"alert": "{{title}}", "severity": "{{level}}"}',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

