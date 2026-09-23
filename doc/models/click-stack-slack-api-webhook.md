
# Click Stack Slack Api Webhook

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSlackApiWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Webhook ID |
| `name` | `str` | Required | Webhook name |
| `service` | `str` | Required, Constant | Webhook service type<br><br>**Value**: `"slack_api"` |
| `url` | `str` | Optional | Slack API endpoint URL |
| `description` | `str` | Optional | Webhook description, shown in the UI |
| `updated_at` | `datetime` | Required | Last update timestamp |
| `created_at` | `datetime` | Required | Creation timestamp |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_slack_api_webhook import ClickStackSlackApiWebhook

click_stack_slack_api_webhook = ClickStackSlackApiWebhook(
    id='65f5e4a3b9e77c001a789012',
    name='Slack Alerts',
    updated_at=dateutil.parser.parse('2025-01-15T12:00:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://hooks.slack.com/services/EXAMPLE/WEBHOOK/URL',
    description='Sends alerts to #engineering channel',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

