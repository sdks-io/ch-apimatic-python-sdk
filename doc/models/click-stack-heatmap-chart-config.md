
# Click Stack Heatmap Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackHeatmapChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "heatmap" for heatmap tiles.<br><br>**Value**: `"heatmap"` |
| `source_id` | `str` | Required | ID of the data source to query. |
| `select` | [`List[ClickStackHeatmapSelectItem]`](../../doc/models/click-stack-heatmap-select-item.md) | Required | Exactly one heatmap select item. |
| `where` | `str` | Optional | Row-level filter (syntax depends on whereLanguage). |
| `where_language` | [`WhereLanguage4`](../../doc/models/where-language-4.md) | Optional | Query language for the where clause. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_heatmap_chart_config import ClickStackHeatmapChartConfig
from openapispecforclickhousecloud.models.click_stack_heatmap_select_item import ClickStackHeatmapSelectItem
from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.heatmap_scale_type import HeatmapScaleType
from openapispecforclickhousecloud.models.output import Output
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_heatmap_chart_config = ClickStackHeatmapChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select=[
        ClickStackHeatmapSelectItem(
            value_expression='Duration',
            count_expression='count()',
            heatmap_scale_type=HeatmapScaleType.LOG,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    where='ServiceName = \'api\'',
    where_language=WhereLanguage4.SQL,
    number_format=ClickStackNumberFormat(
        output=Output.CURRENCY,
        mantissa=170,
        thousand_separated=False,
        average=False,
        decimal_bytes=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

