
# Click Pipe Post Object Storage Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostObjectStorageSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type5`](../../doc/models/type-5.md) | Optional | Type of the ObjectStorage source. |
| `format` | [`Format4`](../../doc/models/format-4.md) | Optional | Format of the files. |
| `url` | `str` | Optional | Provide a path to the file(s) you want to ingest. You can specify multiple files using bash-like wildcards. For more information, see the documentation on using wildcards in path: https://clickhouse.com/docs/en/integrations/clickpipes/object-storage#limitations |
| `delimiter` | `str` | Optional | Delimiter used in the files. |
| `compression` | [`Compression`](../../doc/models/compression.md) | Optional | Compression algorithm used for the files. |
| `is_continuous` | `bool` | Optional | If set to true, the pipe will continuously read new files from the source. If set to false, the pipe will read the files only once. New files have to be uploaded lexically order. |
| `queue_url` | `str` | Optional | Queue URL for event-based continuous ingestion. For S3, provide an SQS queue URL. For GCS, provide a Pub/Sub subscription (e.g. projects/{project}/subscriptions/{name}). When provided, files are ingested based on event notifications rather than lexicographical order. Only applicable when isContinuous is true and authentication is not public. |
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

from openapispecforclickhousecloud.models.click_pipe_post_object_storage_source import ClickPipePostObjectStorageSource
from openapispecforclickhousecloud.models.compression import Compression
from openapispecforclickhousecloud.models.format_4 import Format4
from openapispecforclickhousecloud.models.type_5 import Type5

click_pipe_post_object_storage_source = ClickPipePostObjectStorageSource(
    mtype=Type5.S3,
    format=Format4.JSONEACHROW,
    url='https://datasets-documentation.s3.eu-west-3.amazonaws.com/http/**.ndjson.gz',
    delimiter=',',
    compression=Compression.AUTO,
    queue_url='https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue',
    start_after='events/2026-06-01/',
    iam_role='arn:aws:iam::123456789012:role/MyRole',
    connection_string='DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;EndpointSuffix=core.windows.net',
    path='data/logs/*.json',
    azure_container_name='mycontainer',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

