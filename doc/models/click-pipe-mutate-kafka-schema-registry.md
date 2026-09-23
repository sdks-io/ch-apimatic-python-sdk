
# Click Pipe Mutate Kafka Schema Registry

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeMutateKafkaSchemaRegistry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Schema URL. HTTPS required. |
| `authentication` | [`Authentication`](../../doc/models/authentication.md) | Optional | Authentication type of the schema registry. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificates to validate the schema registry's certificate. |
| `credentials` | [`ClickPipeKafkaSchemaRegistryCredentials`](../../doc/models/click-pipe-kafka-schema-registry-credentials.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication import Authentication
from openapispecforclickhousecloud.models.click_pipe_kafka_schema_registry_credentials import ClickPipeKafkaSchemaRegistryCredentials
from openapispecforclickhousecloud.models.click_pipe_mutate_kafka_schema_registry import ClickPipeMutateKafkaSchemaRegistry

click_pipe_mutate_kafka_schema_registry = ClickPipeMutateKafkaSchemaRegistry(
    url='https://psrc-aa00.us-east-2.aws.confluent.cloud/schemas/ids/100004',
    authentication=Authentication.PLAIN,
    ca_certificate='caCertificate0',
    credentials=ClickPipeKafkaSchemaRegistryCredentials(
        username='username4',
        password='password0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

