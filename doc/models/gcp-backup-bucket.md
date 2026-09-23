
# Gcp Backup Bucket

*This model accepts additional fields of type Any.*

## Structure

`GcpBackupBucket`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique backup bucket ID |
| `bucket_provider` | [`BucketProvider1`](../../doc/models/bucket-provider-1.md) | Optional | Bucket provider |
| `bucket_path` | `str` | Optional | Bucket path |
| `access_key_id` | `str` | Optional | Access Key ID (HMAC key) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.bucket_provider_1 import BucketProvider1
from openapispecforclickhousecloud.models.gcp_backup_bucket import GcpBackupBucket

gcp_backup_bucket = GcpBackupBucket(
    id='00000156-0000-0000-0000-000000000000',
    bucket_provider=BucketProvider1.GCP,
    bucket_path='bucketPath6',
    access_key_id='accessKeyId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

