
# V1 Organizations Services Clickstack Webhooks Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackWebhooksResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [ClickStackSlackWebhook](../../doc/models/click-stack-slack-webhook.md) \| [ClickStackIncidentIOWebhook](../../doc/models/click-stack-incident-io-webhook.md) \| [ClickStackGenericWebhook](../../doc/models/click-stack-generic-webhook.md) \| [ClickStackSlackAPIWebhook](../../doc/models/click-stack-slack-api-webhook.md) \| [ClickStackPagerDutyAPIWebhook](../../doc/models/click-stack-pager-duty-api-webhook.md) \| None | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_slack_webhook import ClickStackSlackWebhook
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_webhooks_response_1 import V1OrganizationsServicesClickstackWebhooksResponse1

v_1_organizations_services_clickstack_webhooks_response_1 = V1OrganizationsServicesClickstackWebhooksResponse1(
    status=200,
    request_id='00001a0c-0000-0000-0000-000000000000',
    result=ClickStackSlackWebhook(
        id='id0',
        name='name0',
        updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        url='url4',
        description='description0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

