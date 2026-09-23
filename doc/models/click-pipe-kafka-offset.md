
# Click Pipe Kafka Offset

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeKafkaOffset`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `strategy` | [`Strategy`](../../doc/models/strategy.md) | Optional | Offset strategy. |
| `timestamp` | `str` | Optional | A minute precision UTC timestamp to start from. Required for "from_timestamp" strategy. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_kafka_offset import ClickPipeKafkaOffset
from openapispecforclickhousecloud.models.strategy import Strategy

click_pipe_kafka_offset = ClickPipeKafkaOffset(
    strategy=Strategy.FROM_BEGINNING,
    timestamp='2021-01-01T00:00',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

