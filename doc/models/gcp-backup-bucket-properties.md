
# Gcp Backup Bucket Properties

*This model accepts additional fields of type Any.*

## Structure

`GcpBackupBucketProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket_provider` | [`BucketProvider1`](../../doc/models/bucket-provider-1.md) | Optional | Bucket provider |
| `bucket_path` | `str` | Optional | Bucket path |
| `access_key_id` | `str` | Optional | Access Key ID (HMAC key) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.bucket_provider_1 import BucketProvider1
from openapispecforclickhousecloud.models.gcp_backup_bucket_properties import GcpBackupBucketProperties

gcp_backup_bucket_properties = GcpBackupBucketProperties(
    bucket_provider=BucketProvider1.GCP,
    bucket_path='bucketPath4',
    access_key_id='accessKeyId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

