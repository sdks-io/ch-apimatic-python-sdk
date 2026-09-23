
# Click Stack Incident Io Webhook

*This model accepts additional fields of type Any.*

## Structure

`ClickStackIncidentIoWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Webhook ID |
| `name` | `str` | Required | Webhook name |
| `service` | `str` | Required, Constant | Webhook service type<br><br>**Value**: `"incidentio"` |
| `url` | `str` | Optional | incident.io alert event HTTP source URL |
| `description` | `str` | Optional | Webhook description, shown in the UI |
| `updated_at` | `datetime` | Required | Last update timestamp |
| `created_at` | `datetime` | Required | Creation timestamp |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_incident_io_webhook import ClickStackIncidentIoWebhook

click_stack_incident_io_webhook = ClickStackIncidentIoWebhook(
    id='507f1f77bcf86cd799439012',
    name='Incident Response',
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://api.incident.io/v2/alert_events/http/abc123',
    description='Routes alerts to incident.io for on-call escalation',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

