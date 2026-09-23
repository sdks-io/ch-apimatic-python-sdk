
# Click Pipe Post Pub Sub Service Account Source

## Structure

`ClickPipePostPubSubServiceAccountSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `format` | [`Format6`](../../doc/models/format-6.md) | Required | Format of messages in the Pub/Sub topic. GCP Pub/Sub ClickPipes are in limited preview — contact support to enable this feature for your organization. |
| `project_id` | `str` | Required | GCP project ID that owns the Pub/Sub topic. |
| `topic` | `str` | Required | Pub/Sub topic name (not the fully-qualified path). |
| `authentication` | `str` | Required, Constant | Authenticate with a GCP service account JSON key.<br><br>**Value**: `"SERVICE_ACCOUNT"` |
| `seek_type` | [`SeekType`](../../doc/models/seek-type.md) | Required | Starting position strategy for consuming the subscription. The seekTimestamp companion is required only when seekType is "timestamp"; setting it for a mismatched seek type is rejected. |
| `seek_timestamp` | `datetime` | Optional | RFC 3339 / ISO 8601 timestamp to seek to. Required when seekType is "timestamp"; must be omitted otherwise. |
| `filter` | `str` | Optional | Optional Pub/Sub subscription filter expression (CEL). Maximum 256 characters.<br><br>**Constraints**: *Maximum Length*: `256` |
| `enable_ordering` | `bool` | Optional | Whether to enable ordered delivery of messages (requires messages to be published with ordering keys). |
| `ack_deadline` | `int` | Optional | Acknowledgement deadline for messages, in seconds. Must be between 10 and 600.<br><br>**Constraints**: `>= 10`, `<= 600` |
| `service_account_key` | [`ServiceAccount`](../../doc/models/service-account.md) | Required | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_post_pub_sub_service_account_source import ClickPipePostPubSubServiceAccountSource
from openapispecforclickhousecloud.models.format_6 import Format6
from openapispecforclickhousecloud.models.seek_type import SeekType
from openapispecforclickhousecloud.models.service_account import ServiceAccount

click_pipe_post_pub_sub_service_account_source = ClickPipePostPubSubServiceAccountSource(
    format=Format6.JSONEACHROW,
    project_id='my-gcp-project',
    topic='my-topic',
    seek_type=SeekType.EARLIEST,
    service_account_key=ServiceAccount(
        service_account_file='serviceAccountFile8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    seek_timestamp=dateutil.parser.parse('2026-04-10T12:00:00Z'),
    filter='filter2',
    enable_ordering=False,
    ack_deadline=188
)
```

