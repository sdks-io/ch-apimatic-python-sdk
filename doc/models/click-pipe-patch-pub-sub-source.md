
# Click Pipe Patch Pub Sub Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchPubSubSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication` | [`Authentication17`](../../doc/models/authentication-17.md) | Required | Authentication method to use with GCP Pub/Sub. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the source resources. |
| `ack_deadline` | `int` | Optional | Acknowledgement deadline for messages, in seconds. Must be between 10 and 600.<br><br>**Constraints**: `>= 10`, `<= 600` |
| `service_account_key` | [`ServiceAccount`](../../doc/models/service-account.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_17 import Authentication17
from openapispecforclickhousecloud.models.click_pipe_patch_pub_sub_source import ClickPipePatchPubSubSource
from openapispecforclickhousecloud.models.service_account import ServiceAccount

click_pipe_patch_pub_sub_source = ClickPipePatchPubSubSource(
    authentication=Authentication17.SERVICE_ACCOUNT,
    ack_deadline=10,
    service_account_key=ServiceAccount(
        service_account_file='serviceAccountFile8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

