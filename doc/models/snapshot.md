
# Snapshot

*This model accepts additional fields of type Any.*

## Structure

`Snapshot`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique snapshot ID. |
| `status` | [`Status2`](../../doc/models/status-2.md) | Optional | Status of the snapshot: 'done', 'error', 'in_progress', 'throttled'. 'throttled' means snapshot creation was rate-limited and will be retried. |
| `service_id` | `str` | Optional | ID of the service the snapshot was created from. |
| `started_at` | `datetime` | Optional | Snapshot start timestamp. ISO-8601. |
| `finished_at` | `datetime` | Optional | Snapshot finish timestamp. ISO-8601. Available only for finished snapshots |
| `size_in_bytes` | `float` | Optional | Size of the snapshot in bytes. |
| `duration_in_seconds` | `float` | Optional | Time in seconds it took to perform the snapshot. If the status is in_progress or throttled, this is the time in seconds since the snapshot started until now. |
| `mtype` | [`Type14`](../../doc/models/type-14.md) | Optional | Snapshot type. Always "full" — snapshots never chain off a parent. |
| `backup_name` | `str` | Optional | Snapshot name on the external backup bucket. |
| `bucket` | [AwsBackupBucketProperties](../../doc/models/aws-backup-bucket-properties.md) \| [GcpBackupBucketProperties](../../doc/models/gcp-backup-bucket-properties.md) \| [AzureBackupBucketProperties](../../doc/models/azure-backup-bucket-properties.md) \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.snapshot import Snapshot
from openapispecforclickhousecloud.models.status_2 import Status2

snapshot = Snapshot(
    id='00000ed6-0000-0000-0000-000000000000',
    status=Status2.IN_PROGRESS,
    service_id='serviceId2',
    started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    finished_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

