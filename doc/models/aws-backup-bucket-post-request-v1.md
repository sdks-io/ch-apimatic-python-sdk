
# Aws Backup Bucket Post Request V1

*This model accepts additional fields of type Any.*

## Structure

`AwsBackupBucketPostRequestV1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket_provider` | [`BucketProvider`](../../doc/models/bucket-provider.md) | Optional | Bucket provider |
| `bucket_path` | `str` | Optional | Bucket path |
| `iam_role_arn` | `str` | Optional | AWS Role ARN |
| `iam_role_session_name` | `str` | Optional | AWS Role session name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.aws_backup_bucket_post_request_v_1 import AwsBackupBucketPostRequestV1
from openapispecforclickhousecloud.models.bucket_provider import BucketProvider

aws_backup_bucket_post_request_v_1 = AwsBackupBucketPostRequestV1(
    bucket_provider=BucketProvider.AWS,
    bucket_path='bucketPath2',
    iam_role_arn='iamRoleArn2',
    iam_role_session_name='iamRoleSessionName0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

