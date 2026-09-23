
# Click Stack Heatmap Select Item

*This model accepts additional fields of type Any.*

## Structure

`ClickStackHeatmapSelectItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value_expression` | `str` | Required | SQL expression for the value being bucketed on the y-axis. Must be non-empty. |
| `count_expression` | `str` | Optional | SQL expression for the count contributing to each bucket. Defaults to "count()" in the editor when omitted. |
| `heatmap_scale_type` | [`HeatmapScaleType`](../../doc/models/heatmap-scale-type.md) | Optional | Scale type used to bucket values on the y-axis. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_heatmap_select_item import ClickStackHeatmapSelectItem
from openapispecforclickhousecloud.models.heatmap_scale_type import HeatmapScaleType

click_stack_heatmap_select_item = ClickStackHeatmapSelectItem(
    value_expression='Duration',
    count_expression='count()',
    heatmap_scale_type=HeatmapScaleType.LOG,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

