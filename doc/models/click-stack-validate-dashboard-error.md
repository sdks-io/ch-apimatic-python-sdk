
# Click Stack Validate Dashboard Error

*This model accepts additional fields of type Any.*

## Structure

`ClickStackValidateDashboardError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `path` | `str` | Required | Dot-separated field path, or empty string for top-level errors. |
| `message` | `str` | Required | Human-readable error description. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_validate_dashboard_error import ClickStackValidateDashboardError

click_stack_validate_dashboard_error = ClickStackValidateDashboardError(
    path='tiles.0.config',
    message='Required',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

