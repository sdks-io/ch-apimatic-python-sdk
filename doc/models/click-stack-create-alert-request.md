
# Click Stack Create Alert Request

*This model accepts additional fields of type Any.*

## Structure

`ClickStackCreateAlertRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dashboard_id` | `str` | Optional | Dashboard ID for tile-based alerts. |
| `tile_id` | `str` | Optional | Tile ID for tile-based alerts. Must be a line, stacked bar, or number type tile. |
| `saved_search_id` | `str` | Optional | Saved search ID for saved_search alerts. |
| `group_by` | `str` | Optional | Group-by key for saved search alerts. |
| `threshold` | `float` | Optional | Threshold value for triggering the alert. For between and not_between threshold types, this is the lower bound. |
| `threshold_max` | `float` | Optional | Upper bound for between and not_between threshold types. Required when thresholdType is between or not_between, must be >= threshold. |
| `interval` | [`Interval`](../../doc/models/interval.md) | Optional | Evaluation interval for the alert. `30s` requires the 30s alert interval feature to be enabled for your team. |
| `schedule_offset_minutes` | `int` | Optional | Offset from the interval boundary in minutes. For example, 2 with a 5m interval evaluates windows at :02, :07, :12, etc. (UTC). |
| `schedule_start_at` | `datetime` | Optional | Absolute UTC start time anchor. Alert windows start from this timestamp and repeat every interval. |
| `source` | [`Source`](../../doc/models/source.md) | Optional | Alert source type (tile-based or saved search). |
| `threshold_type` | [`ThresholdType`](../../doc/models/threshold-type.md) | Optional | Threshold comparison direction. |
| `channel` | [ClickStackAlertChannelEmail](../../doc/models/click-stack-alert-channel-email.md) \| [ClickStackAlertChannelWebhook](../../doc/models/click-stack-alert-channel-webhook.md) \| None | Optional | - |
| `channels` | List[[ClickStackAlertChannelEmail](../../doc/models/click-stack-alert-channel-email.md) \| [ClickStackAlertChannelWebhook](../../doc/models/click-stack-alert-channel-webhook.md)] \| None | Optional | Notification channels to trigger when the alert fires or resolves. Between 1 and 10 channels; duplicates are rejected.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `10` |
| `name` | `str` | Optional | Human-friendly alert name. |
| `message` | `str` | Optional | Alert message template. |
| `note` | `str` | Optional | Freeform note for the alert. Supports markdown formatting. |
| `num_consecutive_windows` | `int` | Optional | Fire the alert only after its condition has been met for this many consecutive evaluation windows. While the condition is met but fewer than this many consecutive windows have violated, the alert is in the PENDING state. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_create_alert_request import ClickStackCreateAlertRequest
from openapispecforclickhousecloud.models.interval import Interval
from openapispecforclickhousecloud.models.source import Source
from openapispecforclickhousecloud.models.threshold_type import ThresholdType

click_stack_create_alert_request = ClickStackCreateAlertRequest(
    dashboard_id='65f5e4a3b9e77c001a567890',
    tile_id='65f5e4a3b9e77c001a901234',
    saved_search_id='65f5e4a3b9e77c001a345678',
    group_by='ServiceName',
    threshold=100,
    threshold_max=500,
    interval=Interval.ENUM_1H,
    schedule_offset_minutes=2,
    schedule_start_at=dateutil.parser.parse('2026-02-08T10:00:00Z'),
    source=Source.TILE,
    threshold_type=ThresholdType.ABOVE,
    name='Test Alert',
    message='Test Alert Message',
    note='Threshold raised from 50 to 100 on 2026-01-15. See [runbook](https://wiki.example.com/runbook).',
    num_consecutive_windows=3,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

