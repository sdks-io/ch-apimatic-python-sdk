
# Click Pipe Patch Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kafka` | [`ClickPipePatchKafkaSource`](../../doc/models/click-pipe-patch-kafka-source.md) | Optional | - |
| `object_storage` | [`ClickPipePatchObjectStorageSource`](../../doc/models/click-pipe-patch-object-storage-source.md) | Optional | - |
| `kinesis` | [`ClickPipePatchKinesisSource`](../../doc/models/click-pipe-patch-kinesis-source.md) | Optional | - |
| `pubsub` | [`ClickPipePatchPubSubSource`](../../doc/models/click-pipe-patch-pub-sub-source.md) | Optional | - |
| `postgres` | [`ClickPipePatchPostgresSource`](../../doc/models/click-pipe-patch-postgres-source.md) | Optional | - |
| `mysql` | [`ClickPipePatchMySqlSource`](../../doc/models/click-pipe-patch-my-sql-source.md) | Optional | - |
| `mongodb` | [`ClickPipePatchMongoDbSource`](../../doc/models/click-pipe-patch-mongo-db-source.md) | Optional | - |
| `validate_samples` | `bool` | Optional | Validate data samples received from data source. It will validate the connection and data availability and correctness. If not enabled, only connection will be validated. This has no effect on Postgres or MySQL pipes, they always only validate the connection and table definitions. This is experimental and can be removed in the future. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_17 import Authentication17
from openapispecforclickhousecloud.models.authentication_2 import Authentication2
from openapispecforclickhousecloud.models.authentication_5 import Authentication5
from openapispecforclickhousecloud.models.authentication_8 import Authentication8
from openapispecforclickhousecloud.models.click_pipe_patch_kafka_source import ClickPipePatchKafkaSource
from openapispecforclickhousecloud.models.click_pipe_patch_kinesis_source import ClickPipePatchKinesisSource
from openapispecforclickhousecloud.models.click_pipe_patch_object_storage_source import ClickPipePatchObjectStorageSource
from openapispecforclickhousecloud.models.click_pipe_patch_postgres_source import ClickPipePatchPostgresSource
from openapispecforclickhousecloud.models.click_pipe_patch_pub_sub_source import ClickPipePatchPubSubSource
from openapispecforclickhousecloud.models.click_pipe_patch_source import ClickPipePatchSource
from openapispecforclickhousecloud.models.msk_iam_user import MskIamUser
from openapispecforclickhousecloud.models.plain import Plain
from openapispecforclickhousecloud.models.service_account import ServiceAccount

click_pipe_patch_source = ClickPipePatchSource(
    kafka=ClickPipePatchKafkaSource(
        authentication=Authentication2.PLAIN,
        iam_role='iamRole6',
        ca_certificate='caCertificate2',
        reverse_private_endpoint_ids=[
            'reversePrivateEndpointIds8'
        ],
        credentials=Plain(
            username='username6',
            password='password8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    object_storage=ClickPipePatchObjectStorageSource(
        skip_initial_load=False,
        start_after='startAfter6',
        authentication=Authentication8.IAM_USER,
        iam_role='iamRole6',
        connection_string='connectionString6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    kinesis=ClickPipePatchKinesisSource(
        authentication=Authentication5.IAM_ROLE,
        iam_role='iamRole8',
        access_key=MskIamUser(
            access_key_id='accessKeyId8',
            secret_key='secretKey6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    pubsub=ClickPipePatchPubSubSource(
        authentication=Authentication17.SERVICE_ACCOUNT,
        ack_deadline=104,
        service_account_key=ServiceAccount(
            service_account_file='serviceAccountFile8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    postgres=ClickPipePatchPostgresSource(
        credentials=Plain(
            username='username4',
            password='password0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        host='host2',
        port=80,
        database='database0',
        tls_host='tlsHost4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

