
# Click Stack Dashboard Container Tab

*This model accepts additional fields of type Any.*

## Structure

`ClickStackDashboardContainerTab`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique identifier for the tab within its container. |
| `title` | `str` | Required | Display title for the tab. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_dashboard_container_tab import ClickStackDashboardContainerTab

click_stack_dashboard_container_tab = ClickStackDashboardContainerTab(
    id='errors',
    title='Errors',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

