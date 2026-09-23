
# Click Pipe Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kafka` | [`ClickPipeKafkaSource`](../../doc/models/click-pipe-kafka-source.md) | Optional | - |
| `object_storage` | [`ClickPipeObjectStorageSource`](../../doc/models/click-pipe-object-storage-source.md) | Optional | - |
| `kinesis` | [`ClickPipeKinesisSource`](../../doc/models/click-pipe-kinesis-source.md) | Optional | - |
| `pubsub` | [`ClickPipePubSubSource`](../../doc/models/click-pipe-pub-sub-source.md) | Optional | - |
| `postgres` | [`ClickPipePostgresSource`](../../doc/models/click-pipe-postgres-source.md) | Optional | - |
| `mysql` | [`ClickPipeMySqlSource`](../../doc/models/click-pipe-my-sql-source.md) | Optional | - |
| `bigquery` | `Any` | Optional | - |
| `mongodb` | [`ClickPipeMongoDbSource`](../../doc/models/click-pipe-mongo-db-source.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.authentication_11 import Authentication11
from openapispecforclickhousecloud.models.authentication_17 import Authentication17
from openapispecforclickhousecloud.models.click_pipe_kafka_source import ClickPipeKafkaSource
from openapispecforclickhousecloud.models.click_pipe_kinesis_source import ClickPipeKinesisSource
from openapispecforclickhousecloud.models.click_pipe_object_storage_source import ClickPipeObjectStorageSource
from openapispecforclickhousecloud.models.click_pipe_postgres_source import ClickPipePostgresSource
from openapispecforclickhousecloud.models.click_pipe_pub_sub_source import ClickPipePubSubSource
from openapispecforclickhousecloud.models.click_pipe_source import ClickPipeSource
from openapispecforclickhousecloud.models.compression import Compression
from openapispecforclickhousecloud.models.format import Format
from openapispecforclickhousecloud.models.format_2 import Format2
from openapispecforclickhousecloud.models.format_4 import Format4
from openapispecforclickhousecloud.models.format_6 import Format6
from openapispecforclickhousecloud.models.iterator_type import IteratorType
from openapispecforclickhousecloud.models.seek_type import SeekType
from openapispecforclickhousecloud.models.type_3 import Type3
from openapispecforclickhousecloud.models.type_5 import Type5
from openapispecforclickhousecloud.models.type_7 import Type7

click_pipe_source = ClickPipeSource(
    kafka=ClickPipeKafkaSource(
        mtype=Type3.AZUREEVENTHUB,
        format=Format.AVROCONFLUENT,
        brokers='brokers4',
        topics='topics8',
        consumer_group='consumerGroup8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    object_storage=ClickPipeObjectStorageSource(
        mtype=Type5.S3,
        format=Format4.CSV,
        url='url6',
        delimiter='delimiter4',
        compression=Compression.LZMA,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    kinesis=ClickPipeKinesisSource(
        format=Format2.JSONEACHROW,
        stream_name='streamName0',
        region='region2',
        use_enhanced_fan_out=False,
        iterator_type=IteratorType.TRIM_HORIZON,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    pubsub=ClickPipePubSubSource(
        format=Format6.JSONEACHROW,
        project_id='projectId8',
        topic='topic0',
        authentication=Authentication17.SERVICE_ACCOUNT,
        seek_type=SeekType.LATEST,
        seek_timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        filter='filter6',
        enable_ordering=False,
        ack_deadline=104,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    postgres=ClickPipePostgresSource(
        mtype=Type7.CRUNCHYBRIDGE,
        host='host2',
        port=80,
        database='database0',
        authentication=Authentication11.BASIC,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

