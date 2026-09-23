
# Authentication 17

Authentication method to use with GCP Pub/Sub. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the source resources.

## Enumeration

`Authentication17`

## Fields

| Name |
|  --- |
| `SERVICE_ACCOUNT` |
| `SERVICE_ACCOUNT_WORKLOAD_IDENTITY` |

## Example

```python
from openapispecforclickhousecloud.models.authentication_17 import Authentication17

authentication_17 = Authentication17.SERVICE_ACCOUNT
```

