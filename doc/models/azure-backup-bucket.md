
# Azure Backup Bucket

*This model accepts additional fields of type Any.*

## Structure

`AzureBackupBucket`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique backup bucket ID. |
| `bucket_provider` | [`BucketProvider2`](../../doc/models/bucket-provider-2.md) | Optional | Bucket provider |
| `container_name` | `str` | Optional | Container Name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.azure_backup_bucket import AzureBackupBucket
from openapispecforclickhousecloud.models.bucket_provider_2 import BucketProvider2

azure_backup_bucket = AzureBackupBucket(
    id='000007b6-0000-0000-0000-000000000000',
    bucket_provider=BucketProvider2.AZURE,
    container_name='containerName8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

