
# Click Pipes Service Context

*This model accepts additional fields of type Any.*

## Structure

`ClickPipesServiceContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gcp_workload_identity` | [`ClickPipesGcpWorkloadIdentityContext`](../../doc/models/click-pipes-gcp-workload-identity-context.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipes_gcp_workload_identity_context import ClickPipesGcpWorkloadIdentityContext
from openapispecforclickhousecloud.models.click_pipes_service_context import ClickPipesServiceContext

click_pipes_service_context = ClickPipesServiceContext(
    gcp_workload_identity=ClickPipesGcpWorkloadIdentityContext(
        supported=False,
        ready=False,
        principal='principal0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

