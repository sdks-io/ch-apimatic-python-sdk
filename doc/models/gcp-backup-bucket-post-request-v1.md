
# Gcp Backup Bucket Post Request V1

*This model accepts additional fields of type Any.*

## Structure

`GcpBackupBucketPostRequestV1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket_provider` | [`BucketProvider1`](../../doc/models/bucket-provider-1.md) | Optional | Bucket provider |
| `bucket_path` | `str` | Optional | Bucket path |
| `access_key_id` | `str` | Optional | Access Key ID (HMAC key) |
| `secret_access_key` | `str` | Optional | Secret Access Key (HMAC secret key) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.bucket_provider_1 import BucketProvider1
from openapispecforclickhousecloud.models.gcp_backup_bucket_post_request_v_1 import GcpBackupBucketPostRequestV1

gcp_backup_bucket_post_request_v_1 = GcpBackupBucketPostRequestV1(
    bucket_provider=BucketProvider1.GCP,
    bucket_path='bucketPath0',
    access_key_id='accessKeyId4',
    secret_access_key='secretAccessKey8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

