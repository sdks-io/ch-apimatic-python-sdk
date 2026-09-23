
# Click Pipe Kafka Schema Registry

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeKafkaSchemaRegistry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Schema URL. HTTPS required. |
| `authentication` | [`Authentication`](../../doc/models/authentication.md) | Optional | Authentication type of the schema registry. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificates to validate the schema registry's certificate. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication import Authentication
from openapispecforclickhousecloud.models.click_pipe_kafka_schema_registry import ClickPipeKafkaSchemaRegistry

click_pipe_kafka_schema_registry = ClickPipeKafkaSchemaRegistry(
    url='https://psrc-aa00.us-east-2.aws.confluent.cloud/schemas/ids/100004',
    authentication=Authentication.PLAIN,
    ca_certificate='caCertificate4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

