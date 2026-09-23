
# Click Pipe Kafka Schema Registry Credentials

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeKafkaSchemaRegistryCredentials`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Optional | Username for the schema registry. |
| `password` | `str` | Optional | Password for the schema registry. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_kafka_schema_registry_credentials import ClickPipeKafkaSchemaRegistryCredentials

click_pipe_kafka_schema_registry_credentials = ClickPipeKafkaSchemaRegistryCredentials(
    username='username6',
    password='password0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

