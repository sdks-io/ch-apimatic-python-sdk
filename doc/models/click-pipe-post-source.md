
# Click Pipe Post Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kafka` | [`ClickPipePostKafkaSource`](../../doc/models/click-pipe-post-kafka-source.md) | Optional | - |
| `object_storage` | [`ClickPipePostObjectStorageSource`](../../doc/models/click-pipe-post-object-storage-source.md) | Optional | - |
| `kinesis` | [`ClickPipePostKinesisSource`](../../doc/models/click-pipe-post-kinesis-source.md) | Optional | - |
| `pubsub` | `Any` | Optional | - |
| `postgres` | [`ClickPipeMutatePostgresSource`](../../doc/models/click-pipe-mutate-postgres-source.md) | Optional | - |
| `mysql` | [`ClickPipeMutateMySqlSource`](../../doc/models/click-pipe-mutate-my-sql-source.md) | Optional | - |
| `bigquery` | `Any` | Optional | - |
| `mongodb` | [`ClickPipeMutateMongoDbSource`](../../doc/models/click-pipe-mutate-mongo-db-source.md) | Optional | - |
| `validate_samples` | `bool` | Optional | Validate data samples received from data source. It will validate the connection and data availability and correctness. If not enabled, only connection will be validated. This has no effect on Postgres or MySQL pipes, they always only validate the connection and table definitions. This is experimental and can be removed in the future. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_mutate_postgres_source import ClickPipeMutatePostgresSource
from openapispecforclickhousecloud.models.click_pipe_post_kafka_source import ClickPipePostKafkaSource
from openapispecforclickhousecloud.models.click_pipe_post_kinesis_source import ClickPipePostKinesisSource
from openapispecforclickhousecloud.models.click_pipe_post_object_storage_source import ClickPipePostObjectStorageSource
from openapispecforclickhousecloud.models.click_pipe_post_source import ClickPipePostSource
from openapispecforclickhousecloud.models.compression import Compression
from openapispecforclickhousecloud.models.format import Format
from openapispecforclickhousecloud.models.format_2 import Format2
from openapispecforclickhousecloud.models.format_4 import Format4
from openapispecforclickhousecloud.models.iterator_type import IteratorType
from openapispecforclickhousecloud.models.plain import Plain
from openapispecforclickhousecloud.models.type_3 import Type3
from openapispecforclickhousecloud.models.type_5 import Type5
from openapispecforclickhousecloud.models.type_7 import Type7

click_pipe_post_source = ClickPipePostSource(
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
)
```

