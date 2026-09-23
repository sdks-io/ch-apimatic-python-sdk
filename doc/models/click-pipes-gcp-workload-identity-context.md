
# Click Pipes Gcp Workload Identity Context

*This model accepts additional fields of type Any.*

## Structure

`ClickPipesGcpWorkloadIdentityContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `supported` | `bool` | Optional | Whether the ClickPipes deployment supports GCP workload identity, which is in Private Preview. The principal field identifies the GCP service account used for source access. |
| `ready` | `bool` | Optional | Whether the service tenant identity is ready for workload identity authentication. |
| `principal` | `str` | Optional | GCP service account used by ClickPipes for workload identity authentication. Grant this service account access to customer source resources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipes_gcp_workload_identity_context import ClickPipesGcpWorkloadIdentityContext

click_pipes_gcp_workload_identity_context = ClickPipesGcpWorkloadIdentityContext(
    supported=False,
    ready=False,
    principal='ch-deadbeef@clickpipes-development.iam.gserviceaccount.com',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

