
# Click Pipe Schema Discovery Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeSchemaDiscoverySource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kafka` | [`ClickPipePostKafkaSource`](../../doc/models/click-pipe-post-kafka-source.md) | Optional | - |
| `kinesis` | [`ClickPipePostKinesisSource`](../../doc/models/click-pipe-post-kinesis-source.md) | Optional | - |
| `pubsub` | `Any` | Optional | - |
| `object_storage` | [`ClickPipePostObjectStorageSource`](../../doc/models/click-pipe-post-object-storage-source.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_post_kafka_source import ClickPipePostKafkaSource
from openapispecforclickhousecloud.models.click_pipe_post_kinesis_source import ClickPipePostKinesisSource
from openapispecforclickhousecloud.models.click_pipe_post_object_storage_source import ClickPipePostObjectStorageSource
from openapispecforclickhousecloud.models.click_pipe_schema_discovery_source import ClickPipeSchemaDiscoverySource
from openapispecforclickhousecloud.models.compression import Compression
from openapispecforclickhousecloud.models.format import Format
from openapispecforclickhousecloud.models.format_2 import Format2
from openapispecforclickhousecloud.models.format_4 import Format4
from openapispecforclickhousecloud.models.iterator_type import IteratorType
from openapispecforclickhousecloud.models.type_3 import Type3
from openapispecforclickhousecloud.models.type_5 import Type5

click_pipe_schema_discovery_source = ClickPipeSchemaDiscoverySource(
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

