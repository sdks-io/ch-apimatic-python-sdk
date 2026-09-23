
# Click Stack Dashboard Container

*This model accepts additional fields of type Any.*

## Structure

`ClickStackDashboardContainer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique identifier for the container within the dashboard. |
| `title` | `str` | Required | Display title for the container. |
| `collapsed` | `bool` | Required | Persisted default collapse state. Per-viewer state lives in the URL. |
| `collapsible` | `bool` | Optional | Whether the user can collapse the group. |
| `bordered` | `bool` | Optional | Whether to show a visual border around the group. |
| `tabs` | [`List[ClickStackDashboardContainerTab]`](../../doc/models/click-stack-dashboard-container-tab.md) | Optional | Optional tabs. 2+ entries renders a tab bar; 0-1 entries renders a plain group header. Tiles join a tab via tabId. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_dashboard_container import ClickStackDashboardContainer
from openapispecforclickhousecloud.models.click_stack_dashboard_container_tab import ClickStackDashboardContainerTab

click_stack_dashboard_container = ClickStackDashboardContainer(
    id='service-health',
    title='Service Health',
    collapsed=False,
    collapsible=True,
    bordered=True,
    tabs=[
        ClickStackDashboardContainerTab(
            id='id8',
            title='title4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackDashboardContainerTab(
            id='id8',
            title='title4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

