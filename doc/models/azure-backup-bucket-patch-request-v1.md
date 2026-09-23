
# Azure Backup Bucket Patch Request V1

*This model accepts additional fields of type Any.*

## Structure

`AzureBackupBucketPatchRequestV1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket_provider` | [`BucketProvider2`](../../doc/models/bucket-provider-2.md) | Optional | Bucket provider |
| `container_name` | `str` | Optional | Container Name |
| `connection_string` | `str` | Optional | Connection String |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.azure_backup_bucket_patch_request_v_1 import AzureBackupBucketPatchRequestV1
from openapispecforclickhousecloud.models.bucket_provider_2 import BucketProvider2

azure_backup_bucket_patch_request_v_1 = AzureBackupBucketPatchRequestV1(
    bucket_provider=BucketProvider2.AZURE,
    container_name='containerName8',
    connection_string='connectionString4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

