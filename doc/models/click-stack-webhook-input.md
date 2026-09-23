
# Click Stack Webhook Input

*This model accepts additional fields of type Any.*

## Structure

`ClickStackWebhookInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Webhook name. Must be unique per service within the team. |
| `service` | [`Service1`](../../doc/models/service-1.md) | Required | Webhook service type. |
| `url` | `str` | Required | Webhook destination URL. |
| `description` | `str` | Optional | Webhook description, shown in the UI. |
| `body` | `str` | Optional | Optional request body template. Only for generic/incidentio; rejected for slack. |
| `headers` | `Dict[str, str]` | Optional | - |
| `query_params` | `Dict[str, str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_webhook_input import ClickStackWebhookInput
from openapispecforclickhousecloud.models.service_1 import Service1

click_stack_webhook_input = ClickStackWebhookInput(
    name='Production Alerts',
    service=Service1.SLACK,
    url='https://hooks.slack.com/services/EXAMPLE/WEBHOOK/URL',
    description='Sends critical alerts to the #incidents channel',
    body='{"alert": "{{title}}", "severity": "{{level}}"}',
    headers={
        'key0': 'headers5',
        'key1': 'headers6',
        'key2': 'headers7'
    },
    query_params={
        'key0': 'queryParams7',
        'key1': 'queryParams8'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

