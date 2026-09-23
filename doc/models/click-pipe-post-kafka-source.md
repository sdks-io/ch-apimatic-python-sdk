
# Click Pipe Post Kafka Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostKafkaSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type3`](../../doc/models/type-3.md) | Optional | Type of the Kafka source. |
| `format` | [`Format`](../../doc/models/format.md) | Optional | Format of the Kafka source. |
| `brokers` | `str` | Optional | Brokers of the Kafka source. |
| `topics` | `str` | Optional | Topics of the Kafka source. |
| `consumer_group` | `str` | Optional | Consumer group of the Kafka source. If not provided "clickpipes-<<ID>>" will be used. |
| `authentication` | [`Authentication2`](../../doc/models/authentication-2.md) | Optional | Authentication method of the Kafka source. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the source resources. Supported authentication methods: kafka: PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, msk: SCRAM-SHA-512, IAM_ROLE, IAM_USER, MUTUAL_TLS, gcmk: PLAIN, MUTUAL_TLS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY, confluent: PLAIN, MUTUAL_TLS, warpstream: PLAIN, azureeventhub: PLAIN, redpanda: SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, dokafka: SCRAM-SHA-256, MUTUAL_TLS |
| `iam_role` | `str` | Optional | IAM role for the Kafka source. Use with IAM role authentication. Read more in ClickPipes documentation: https://clickhouse.com/docs/en/integrations/clickpipes/kafka#iam |
| `offset` | [`ClickPipeKafkaOffset`](../../doc/models/click-pipe-kafka-offset.md) | Optional | - |
| `schema_registry` | [`ClickPipeMutateKafkaSchemaRegistry`](../../doc/models/click-pipe-mutate-kafka-schema-registry.md) | Optional | - |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificates to validate the broker's certificate. |
| `reverse_private_endpoint_ids` | `List[str]` | Optional | Reverse private endpoint UUIDs used for a secure private connection to the Kafka source. |
| `exactly_once` | `bool` | Optional | Enable exactly-once delivery. Guarantees every Kafka record is inserted exactly once across restarts and rebalances. Can only be set at pipe creation. |
| `credentials` | [PLAIN](../../doc/models/plain.md) \| [MskIamUser](../../doc/models/msk-iam-user.md) \| [AzureEventHub](../../doc/models/azure-event-hub.md) \| [MutualTLS](../../doc/models/mutual-tls.md) \| None | Optional | This is a container for one-of cases. |
| `protobuf_schema` | `str` | Optional | Base64-encoded .proto source or serialized FileDescriptorSet. Supported only with Protobuf format and cannot be combined with schemaRegistry.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1048576` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_post_kafka_source import ClickPipePostKafkaSource
from openapispecforclickhousecloud.models.format import Format
from openapispecforclickhousecloud.models.type_3 import Type3

click_pipe_post_kafka_source = ClickPipePostKafkaSource(
    mtype=Type3.MSK,
    format=Format.AVROCONFLUENT,
    brokers='brokers2',
    topics='topics4',
    consumer_group='my-clickpipe-consumer-group',
    iam_role='arn:aws:iam::123456789012:role/MyRole',
    protobuf_schema='c3ludGF4ID0gInByb3RvMyI7IG1lc3NhZ2UgRXZlbnQge30=',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

