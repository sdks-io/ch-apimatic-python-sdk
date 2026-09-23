
# Authentication 2

Authentication method of the Kafka source. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the source resources. Supported authentication methods: kafka: PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, msk: SCRAM-SHA-512, IAM_ROLE, IAM_USER, MUTUAL_TLS, gcmk: PLAIN, MUTUAL_TLS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY, confluent: PLAIN, MUTUAL_TLS, warpstream: PLAIN, azureeventhub: PLAIN, redpanda: SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, dokafka: SCRAM-SHA-256, MUTUAL_TLS

## Enumeration

`Authentication2`

## Fields

| Name |
|  --- |
| `PLAIN` |
| `SCRAMSHA256` |
| `SCRAMSHA512` |
| `IAM_ROLE` |
| `IAM_USER` |
| `MUTUAL_TLS` |
| `SERVICE_ACCOUNT_WORKLOAD_IDENTITY` |

## Example

```python
from openapispecforclickhousecloud.models.authentication_2 import Authentication2

authentication_2 = Authentication2.SCRAMSHA512
```

