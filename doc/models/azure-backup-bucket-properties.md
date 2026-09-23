
# Azure Backup Bucket Properties

*This model accepts additional fields of type Any.*

## Structure

`AzureBackupBucketProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bucket_provider` | [`BucketProvider2`](../../doc/models/bucket-provider-2.md) | Optional | Bucket provider |
| `container_name` | `str` | Optional | Container Name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.azure_backup_bucket_properties import AzureBackupBucketProperties
from openapispecforclickhousecloud.models.bucket_provider_2 import BucketProvider2

azure_backup_bucket_properties = AzureBackupBucketProperties(
    bucket_provider=BucketProvider2.AZURE,
    container_name='containerName0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

