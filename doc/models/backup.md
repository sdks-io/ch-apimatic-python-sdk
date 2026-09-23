
# Backup

*This model accepts additional fields of type Any.*

## Structure

`Backup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique backup ID. |
| `status` | [`Status1`](../../doc/models/status-1.md) | Optional | Status of the backup: 'done', 'error', 'in_progress'. |
| `service_id` | `str` | Optional | Name |
| `started_at` | `datetime` | Optional | Backup start timestamp. ISO-8601. |
| `finished_at` | `datetime` | Optional | Backup finish timestamp. ISO-8601. Available only for finished backups |
| `size_in_bytes` | `float` | Optional | Size of the backup in bytes. |
| `duration_in_seconds` | `float` | Optional | Time in seconds it took to perform the backup. If the status still in_progress, this is the time in seconds since the backup started until now. |
| `mtype` | [`Type13`](../../doc/models/type-13.md) | Optional | Backup type ("full" or "incremental"). |
| `backup_name` | `str` | Optional | Backup name on the external backup bucket. |
| `bucket` | [AwsBackupBucketProperties](../../doc/models/aws-backup-bucket-properties.md) \| [GcpBackupBucketProperties](../../doc/models/gcp-backup-bucket-properties.md) \| [AzureBackupBucketProperties](../../doc/models/azure-backup-bucket-properties.md) \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.backup import Backup
from openapispecforclickhousecloud.models.status_1 import Status1

backup = Backup(
    id='000009d0-0000-0000-0000-000000000000',
    status=Status1.IN_PROGRESS,
    service_id='serviceId6',
    started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    finished_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

