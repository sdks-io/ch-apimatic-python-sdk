
# Aws Backup Bucket

*This model accepts additional fields of type Any.*

## Structure

`AwsBackupBucket`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique backup bucket ID |
| `bucket_provider` | [`BucketProvider`](../../doc/models/bucket-provider.md) | Optional | Bucket provider |
| `bucket_path` | `str` | Optional | Bucket path |
| `iam_role_arn` | `str` | Optional | AWS Role ARN |
| `iam_role_session_name` | `str` | Optional | AWS  Role session name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.aws_backup_bucket import AwsBackupBucket
from openapispecforclickhousecloud.models.bucket_provider import BucketProvider

aws_backup_bucket = AwsBackupBucket(
    id='000012ac-0000-0000-0000-000000000000',
    bucket_provider=BucketProvider.AWS,
    bucket_path='bucketPath2',
    iam_role_arn='iamRoleArn2',
    iam_role_session_name='iamRoleSessionName0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

