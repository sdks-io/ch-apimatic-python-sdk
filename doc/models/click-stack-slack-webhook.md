
# Click Stack Slack Webhook

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSlackWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Webhook ID |
| `name` | `str` | Required | Webhook name |
| `service` | `str` | Required, Constant | Webhook service type<br><br>**Value**: `"slack"` |
| `url` | `str` | Optional | Slack incoming webhook URL |
| `description` | `str` | Optional | Webhook description, shown in the UI |
| `updated_at` | `datetime` | Required | Last update timestamp |
| `created_at` | `datetime` | Required | Creation timestamp |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_slack_webhook import ClickStackSlackWebhook

click_stack_slack_webhook = ClickStackSlackWebhook(
    id='507f1f77bcf86cd799439011',
    name='Production Alerts',
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://hooks.slack.com/services/EXAMPLE/WEBHOOK/URL',
    description='Sends critical alerts to the #incidents channel',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

