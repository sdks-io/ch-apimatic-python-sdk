
# V1 Organizations Services Backup Bucket Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesBackupBucketResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [AwsBackupBucket](../../doc/models/aws-backup-bucket.md) \| [GcpBackupBucket](../../doc/models/gcp-backup-bucket.md) \| [AzureBackupBucket](../../doc/models/azure-backup-bucket.md) \| None | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.aws_backup_bucket import AwsBackupBucket
from openapispecforclickhousecloud.models.bucket_provider import BucketProvider
from openapispecforclickhousecloud.models.v_1_organizations_services_backup_bucket_response import V1OrganizationsServicesBackupBucketResponse

v_1_organizations_services_backup_bucket_response = V1OrganizationsServicesBackupBucketResponse(
    status=200,
    request_id='00001d4e-0000-0000-0000-000000000000',
    result=AwsBackupBucket(
        id='00001a3e-0000-0000-0000-000000000000',
        bucket_provider=BucketProvider.AWS,
        bucket_path='bucketPath0',
        iam_role_arn='iamRoleArn6',
        iam_role_session_name='iamRoleSessionName8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

