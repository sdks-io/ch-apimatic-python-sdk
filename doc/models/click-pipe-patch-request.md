
# Click Pipe Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the ClickPipe. |
| `source` | [`ClickPipePatchSource`](../../doc/models/click-pipe-patch-source.md) | Optional | - |
| `destination` | [`ClickPipePatchDestination`](../../doc/models/click-pipe-patch-destination.md) | Optional | - |
| `field_mappings` | [`List[ClickPipeFieldMapping]`](../../doc/models/click-pipe-field-mapping.md) | Optional | Field mappings of the ClickPipe. This will not update the table schema, only the ClickPipe configuration. |
| `settings` | [`ClickPipeSettings`](../../doc/models/click-pipe-settings.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_17 import Authentication17
from openapispecforclickhousecloud.models.authentication_2 import Authentication2
from openapispecforclickhousecloud.models.authentication_5 import Authentication5
from openapispecforclickhousecloud.models.authentication_8 import Authentication8
from openapispecforclickhousecloud.models.click_pipe_destination_column import ClickPipeDestinationColumn
from openapispecforclickhousecloud.models.click_pipe_field_mapping import ClickPipeFieldMapping
from openapispecforclickhousecloud.models.click_pipe_patch_destination import ClickPipePatchDestination
from openapispecforclickhousecloud.models.click_pipe_patch_kafka_source import ClickPipePatchKafkaSource
from openapispecforclickhousecloud.models.click_pipe_patch_kinesis_source import ClickPipePatchKinesisSource
from openapispecforclickhousecloud.models.click_pipe_patch_object_storage_source import ClickPipePatchObjectStorageSource
from openapispecforclickhousecloud.models.click_pipe_patch_postgres_source import ClickPipePatchPostgresSource
from openapispecforclickhousecloud.models.click_pipe_patch_pub_sub_source import ClickPipePatchPubSubSource
from openapispecforclickhousecloud.models.click_pipe_patch_request import ClickPipePatchRequest
from openapispecforclickhousecloud.models.click_pipe_patch_source import ClickPipePatchSource
from openapispecforclickhousecloud.models.click_pipe_settings import ClickPipeSettings
from openapispecforclickhousecloud.models.msk_iam_user import MskIamUser
from openapispecforclickhousecloud.models.plain import Plain
from openapispecforclickhousecloud.models.service_account import ServiceAccount

click_pipe_patch_request = ClickPipePatchRequest(
    name='name8',
    source=ClickPipePatchSource(
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
    ),
    destination=ClickPipePatchDestination(
        columns=[
            ClickPipeDestinationColumn(
                name='name0',
                mtype='type0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ClickPipeDestinationColumn(
                name='name0',
                mtype='type0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ClickPipeDestinationColumn(
                name='name0',
                mtype='type0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    field_mappings=[
        ClickPipeFieldMapping(
            source_field='sourceField4',
            destination_field='destinationField6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickPipeFieldMapping(
            source_field='sourceField4',
            destination_field='destinationField6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    settings=ClickPipeSettings(
        streaming_max_insert_wait_ms=500,
        object_storage_concurrency=35,
        object_storage_polling_interval_ms=100,
        object_storage_max_insert_bytes=524288000,
        object_storage_max_file_count=30,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

