
# Click Pipe Patch Object Storage Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchObjectStorageSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `skip_initial_load` | `bool` | Optional | If set to true, skips the initial load and only ingests files delivered by queue notifications. Only applicable when queueUrl is provided. |
| `start_after` | `str` | Optional | Skip all files up to and including this object key during the initial load. Cannot be provided when skipInitialLoad is true. |
| `authentication` | [`Authentication8`](../../doc/models/authentication-8.md) | Optional | Authentication method. IAM_USER is for S3, GCS, and DigitalOcean Spaces. IAM_ROLE is for S3 only. SERVICE_ACCOUNT is for GCS only. For GCS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the source resources. CONNECTION_STRING is for Azure Blob Storage. PUBLIC uses no authentication. |
| `iam_role` | `str` | Optional | IAM role to be used with IAM role authentication. Read more in ClickPipes documentation: https://clickhouse.com/docs/en/integrations/clickpipes/object-storage#authentication |
| `connection_string` | `str` | Optional | Connection string for Azure Blob Storage authentication. Required when authentication is CONNECTION_STRING. |
| `path` | `str` | Optional | Path to the file(s) within the Azure container. Used for Azure Blob Storage sources. You can specify multiple files using bash-like wildcards. For more information, see the documentation on using wildcards in path: https://clickhouse.com/docs/en/integrations/clickpipes/object-storage#limitations |
| `azure_container_name` | `str` | Optional | Container name for Azure Blob Storage. Required when type is azureblobstorage. |
| `access_key` | [`MskIamUser`](../../doc/models/msk-iam-user.md) | Optional | - |
| `service_account_key` | `str` | Optional | Base64-encoded GCP service account JSON key. Required when authentication is SERVICE_ACCOUNT. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_8 import Authentication8
from openapispecforclickhousecloud.models.click_pipe_patch_object_storage_source import ClickPipePatchObjectStorageSource

click_pipe_patch_object_storage_source = ClickPipePatchObjectStorageSource(
    skip_initial_load=False,
    start_after='events/2026-06-01/',
    authentication=Authentication8.SERVICE_ACCOUNT,
    iam_role='arn:aws:iam::123456789012:role/MyRole',
    connection_string='DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;EndpointSuffix=core.windows.net',
    path='data/logs/*.json',
    azure_container_name='mycontainer',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

