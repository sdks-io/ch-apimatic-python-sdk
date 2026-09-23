
# Click Pipe Post Pub Sub Workload Identity Source

## Structure

`ClickPipePostPubSubWorkloadIdentitySource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `format` | [`Format6`](../../doc/models/format-6.md) | Required | Format of messages in the Pub/Sub topic. GCP Pub/Sub ClickPipes are in limited preview — contact support to enable this feature for your organization. |
| `project_id` | `str` | Required | GCP project ID that owns the Pub/Sub topic. |
| `topic` | `str` | Required | Pub/Sub topic name (not the fully-qualified path). |
| `authentication` | `str` | Required, Constant | SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the source resources.<br><br>**Value**: `"SERVICE_ACCOUNT_WORKLOAD_IDENTITY"` |
| `seek_type` | [`SeekType`](../../doc/models/seek-type.md) | Required | Starting position strategy for consuming the subscription. The seekTimestamp companion is required only when seekType is "timestamp"; setting it for a mismatched seek type is rejected. |
| `seek_timestamp` | `datetime` | Optional | RFC 3339 / ISO 8601 timestamp to seek to. Required when seekType is "timestamp"; must be omitted otherwise. |
| `filter` | `str` | Optional | Optional Pub/Sub subscription filter expression (CEL). Maximum 256 characters.<br><br>**Constraints**: *Maximum Length*: `256` |
| `enable_ordering` | `bool` | Optional | Whether to enable ordered delivery of messages (requires messages to be published with ordering keys). |
| `ack_deadline` | `int` | Optional | Acknowledgement deadline for messages, in seconds. Must be between 10 and 600.<br><br>**Constraints**: `>= 10`, `<= 600` |

## Example

```python
import dateutil.parser

from openapispecforclickhousecloud.models.click_pipe_post_pub_sub_workload_identity_source import ClickPipePostPubSubWorkloadIdentitySource
from openapispecforclickhousecloud.models.format_6 import Format6
from openapispecforclickhousecloud.models.seek_type import SeekType

click_pipe_post_pub_sub_workload_identity_source = ClickPipePostPubSubWorkloadIdentitySource(
    format=Format6.JSONEACHROW,
    project_id='my-gcp-project',
    topic='my-topic',
    seek_type=SeekType.EARLIEST,
    seek_timestamp=dateutil.parser.parse('2026-04-10T12:00:00Z'),
    filter='filter2',
    enable_ordering=False,
    ack_deadline=18
)
```

