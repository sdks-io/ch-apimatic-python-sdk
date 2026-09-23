
# Click Stack Alert Channel Email

*This model accepts additional fields of type Any.*

## Structure

`ClickStackAlertChannelEmail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type16`](../../doc/models/type-16.md) | Required | Channel type. Must be "email" for email alerts. |
| `email_recipients` | `List[str]` | Required | Email recipients for email alerts. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_alert_channel_email import ClickStackAlertChannelEmail
from openapispecforclickhousecloud.models.type_16 import Type16

click_stack_alert_channel_email = ClickStackAlertChannelEmail(
    mtype=Type16.WEBHOOK,
    email_recipients=[
        'emailRecipients5',
        'emailRecipients4'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

