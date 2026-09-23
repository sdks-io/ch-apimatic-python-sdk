
# Click Stack Validate Dashboard Response

*This model accepts additional fields of type Any.*

## Structure

`ClickStackValidateDashboardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `valid` | `bool` | Required | True when the body passes all validation rules. |
| `errors` | [`List[ClickStackValidateDashboardError]`](../../doc/models/click-stack-validate-dashboard-error.md) | Required | Validation errors. Empty when valid is true. |
| `normalized` | `Any` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_validate_dashboard_error import ClickStackValidateDashboardError
from openapispecforclickhousecloud.models.click_stack_validate_dashboard_response import ClickStackValidateDashboardResponse

click_stack_validate_dashboard_response = ClickStackValidateDashboardResponse(
    valid=False,
    errors=[
        ClickStackValidateDashboardError(
            path='tiles.0.config',
            message='Required',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    normalized=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

