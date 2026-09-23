
# Click Pipe Post Request

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the ClickPipe. |
| `source` | [`ClickPipePostSource`](../../doc/models/click-pipe-post-source.md) | Optional | - |
| `destination` | [`ClickPipeMutateDestination`](../../doc/models/click-pipe-mutate-destination.md) | Optional | - |
| `field_mappings` | [`List[ClickPipeFieldMapping]`](../../doc/models/click-pipe-field-mapping.md) | Optional | Field mappings of the ClickPipe. Note that all destination columns must be included in the mappings. |
| `scaling` | [`ClickPipeScaling`](../../doc/models/click-pipe-scaling.md) | Optional | - |
| `settings` | [`ClickPipeSettings`](../../doc/models/click-pipe-settings.md) | Optional | - |
| `start_paused` | `bool` | Optional | Create the ClickPipe in the Stopped state instead of starting ingestion immediately. Start it later with the state endpoint. Not supported for database ClickPipes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_destination_column import ClickPipeDestinationColumn
from openapispecforclickhousecloud.models.click_pipe_destination_table_definition import ClickPipeDestinationTableDefinition
from openapispecforclickhousecloud.models.click_pipe_destination_table_engine import ClickPipeDestinationTableEngine
from openapispecforclickhousecloud.models.click_pipe_field_mapping import ClickPipeFieldMapping
from openapispecforclickhousecloud.models.click_pipe_mutate_destination import ClickPipeMutateDestination
from openapispecforclickhousecloud.models.click_pipe_mutate_postgres_source import ClickPipeMutatePostgresSource
from openapispecforclickhousecloud.models.click_pipe_post_kafka_source import ClickPipePostKafkaSource
from openapispecforclickhousecloud.models.click_pipe_post_kinesis_source import ClickPipePostKinesisSource
from openapispecforclickhousecloud.models.click_pipe_post_object_storage_source import ClickPipePostObjectStorageSource
from openapispecforclickhousecloud.models.click_pipe_post_request import ClickPipePostRequest
from openapispecforclickhousecloud.models.click_pipe_post_source import ClickPipePostSource
from openapispecforclickhousecloud.models.click_pipe_scaling import ClickPipeScaling
from openapispecforclickhousecloud.models.compression import Compression
from openapispecforclickhousecloud.models.format import Format
from openapispecforclickhousecloud.models.format_2 import Format2
from openapispecforclickhousecloud.models.format_4 import Format4
from openapispecforclickhousecloud.models.iterator_type import IteratorType
from openapispecforclickhousecloud.models.plain import Plain
from openapispecforclickhousecloud.models.type_11 import Type11
from openapispecforclickhousecloud.models.type_3 import Type3
from openapispecforclickhousecloud.models.type_5 import Type5
from openapispecforclickhousecloud.models.type_7 import Type7

click_pipe_post_request = ClickPipePostRequest(
    name='name8',
    source=ClickPipePostSource(
        kafka=ClickPipePostKafkaSource(
            mtype=Type3.AZUREEVENTHUB,
            format=Format.AVROCONFLUENT,
            brokers='brokers4',
            topics='topics8',
            consumer_group='consumerGroup8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        object_storage=ClickPipePostObjectStorageSource(
            mtype=Type5.S3,
            format=Format4.CSV,
            url='url6',
            delimiter='delimiter4',
            compression=Compression.LZMA,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        kinesis=ClickPipePostKinesisSource(
            format=Format2.JSONEACHROW,
            stream_name='streamName0',
            region='region2',
            use_enhanced_fan_out=False,
            iterator_type=IteratorType.TRIM_HORIZON,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        pubsub=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        postgres=ClickPipeMutatePostgresSource(
            mtype=Type7.CRUNCHYBRIDGE,
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
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    destination=ClickPipeMutateDestination(
        database='database4',
        table='table2',
        managed_table=False,
        table_definition=ClickPipeDestinationTableDefinition(
            engine=ClickPipeDestinationTableEngine(
                mtype=Type11.MERGETREE,
                version_column_id='versionColumnId2',
                column_ids=[
                    'columnIds0'
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            sorting_key=[
                'sortingKey0'
            ],
            partition_by='partitionBy0',
            primary_key='primaryKey2',
            ttl='ttl2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
    scaling=ClickPipeScaling(
        replicas=40,
        concurrency=26,
        replica_cpu_millicores=196,
        replica_memory_gb=8,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

