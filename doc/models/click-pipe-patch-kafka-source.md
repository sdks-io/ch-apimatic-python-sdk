
# Click Pipe Patch Kafka Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchKafkaSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication` | [`Authentication2`](../../doc/models/authentication-2.md) | Optional | Authentication method of the Kafka source. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the source resources. Supported authentication methods: kafka: PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, msk: SCRAM-SHA-512, IAM_ROLE, IAM_USER, MUTUAL_TLS, gcmk: PLAIN, MUTUAL_TLS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY, confluent: PLAIN, MUTUAL_TLS, warpstream: PLAIN, azureeventhub: PLAIN, redpanda: SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, dokafka: SCRAM-SHA-256, MUTUAL_TLS |
| `iam_role` | `str` | Optional | IAM role for the Kafka source. Use with IAM role authentication. Read more in ClickPipes documentation: https://clickhouse.com/docs/en/integrations/clickpipes/kafka#iam |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificates to validate the broker's certificate. |
| `reverse_private_endpoint_ids` | `List[str]` | Optional | Reverse private endpoint UUIDs used for a secure private connection to the Kafka source. |
| `credentials` | [PLAIN](../../doc/models/plain.md) \| [MskIamUser](../../doc/models/msk-iam-user.md) \| [AzureEventHub](../../doc/models/azure-event-hub.md) \| [MutualTLS](../../doc/models/mutual-tls.md) \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_2 import Authentication2
from openapispecforclickhousecloud.models.click_pipe_patch_kafka_source import ClickPipePatchKafkaSource
from openapispecforclickhousecloud.models.plain import Plain

click_pipe_patch_kafka_source = ClickPipePatchKafkaSource(
    authentication=Authentication2.PLAIN,
    iam_role='arn:aws:iam::123456789012:role/MyRole',
    ca_certificate='caCertificate8',
    reverse_private_endpoint_ids=[
        'reversePrivateEndpointIds4',
        'reversePrivateEndpointIds3'
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
)
```

