
# Click Stack Alert Channel Webhook

*This model accepts additional fields of type Any.*

## Structure

`ClickStackAlertChannelWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type17`](../../doc/models/type-17.md) | Required | Channel type. Must be "webhook" for webhook alerts. |
| `webhook_id` | `str` | Required | Webhook destination ID. |
| `webhook_service` | `str` | Optional | Webhook service type (e.g., slack_api). |
| `slack_channel_id` | `str` | Optional | Slack channel ID for Slack webhooks. |
| `severity` | [`Severity`](../../doc/models/severity.md) | Optional | Severity label used by PagerDuty API webhooks. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_alert_channel_webhook import ClickStackAlertChannelWebhook
from openapispecforclickhousecloud.models.severity import Severity
from openapispecforclickhousecloud.models.type_17 import Type17

click_stack_alert_channel_webhook = ClickStackAlertChannelWebhook(
    mtype=Type17.WEBHOOK,
    webhook_id='65f5e4a3b9e77c001a789012',
    webhook_service='slack_api',
    slack_channel_id='C01ABCDEF23',
    severity=Severity.WARNING,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

