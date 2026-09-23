
# Click Stack Pager Duty Api Webhook

*This model accepts additional fields of type Any.*

## Structure

`ClickStackPagerDutyApiWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Webhook ID |
| `name` | `str` | Required | Webhook name |
| `service` | `str` | Required, Constant | Webhook service type<br><br>**Value**: `"pagerduty_api"` |
| `url` | `str` | Optional | PagerDuty Events API endpoint URL |
| `description` | `str` | Optional | Webhook description, shown in the UI |
| `updated_at` | `datetime` | Required | Last update timestamp |
| `created_at` | `datetime` | Required | Creation timestamp |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_pager_duty_api_webhook import ClickStackPagerDutyApiWebhook

click_stack_pager_duty_api_webhook = ClickStackPagerDutyApiWebhook(
    id='65f5e4a3b9e77c001a789013',
    name='PagerDuty Alerts',
    updated_at=dateutil.parser.parse('2025-01-15T12:00:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://events.pagerduty.com/v2/enqueue',
    description='Sends critical alerts to PagerDuty',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

