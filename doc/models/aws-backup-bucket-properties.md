
# Aws Backup Bucket Properties

*This model accepts additional fields of type Any.*

## Structure

`AwsBackupBucketProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket_provider` | [`BucketProvider`](../../doc/models/bucket-provider.md) | Optional | Bucket provider |
| `bucket_path` | `str` | Optional | Bucket path |
| `iam_role_arn` | `str` | Optional | AWS IAM Role |
| `iam_role_session_name` | `str` | Optional | AWS IAM Role |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.aws_backup_bucket_properties import AwsBackupBucketProperties
from openapispecforclickhousecloud.models.bucket_provider import BucketProvider

aws_backup_bucket_properties = AwsBackupBucketProperties(
    bucket_provider=BucketProvider.AWS,
    bucket_path='bucketPath0',
    iam_role_arn='iamRoleArn4',
    iam_role_session_name='iamRoleSessionName8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

