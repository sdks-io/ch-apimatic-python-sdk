
# Click Stack Tile Output

*This model accepts additional fields of type Any.*

## Structure

`ClickStackTileOutput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Display name for the tile |
| `x` | `int` | Required | Horizontal position in the grid (0-based) |
| `y` | `int` | Required | Vertical position in the grid (0-based) |
| `w` | `int` | Required | Width in grid units |
| `h` | `int` | Required | Height in grid units |
| `config` | [ClickStackLineBuilderChartConfig](../../doc/models/click-stack-line-builder-chart-config.md) \| [ClickStackLineRawSqlChartConfig](../../doc/models/click-stack-line-raw-sql-chart-config.md) \| [ClickStackBarBuilderChartConfig](../../doc/models/click-stack-bar-builder-chart-config.md) \| [ClickStackBarRawSqlChartConfig](../../doc/models/click-stack-bar-raw-sql-chart-config.md) \| [ClickStackTableBuilderChartConfig](../../doc/models/click-stack-table-builder-chart-config.md) \| [ClickStackTableRawSqlChartConfig](../../doc/models/click-stack-table-raw-sql-chart-config.md) \| [ClickStackNumberBuilderChartConfig](../../doc/models/click-stack-number-builder-chart-config.md) \| [ClickStackNumberRawSqlChartConfig](../../doc/models/click-stack-number-raw-sql-chart-config.md) \| [ClickStackPieBuilderChartConfig](../../doc/models/click-stack-pie-builder-chart-config.md) \| [ClickStackPieRawSqlChartConfig](../../doc/models/click-stack-pie-raw-sql-chart-config.md) \| [ClickStackCategoricalBarBuilderChartConfig](../../doc/models/click-stack-categorical-bar-builder-chart-config.md) \| [ClickStackCategoricalBarRawSqlChartConfig](../../doc/models/click-stack-categorical-bar-raw-sql-chart-config.md) \| [ClickStackHeatmapChartConfig](../../doc/models/click-stack-heatmap-chart-config.md) \| [ClickStackSearchChartConfig](../../doc/models/click-stack-search-chart-config.md) \| [ClickStackEventPatternsChartConfig](../../doc/models/click-stack-event-patterns-chart-config.md) \| [ClickStackMarkdownChartConfig](../../doc/models/click-stack-markdown-chart-config.md) \| None | Optional | - |
| `container_id` | `str` | Optional | References a DashboardContainer by id. Tiles without containerId render in the default ungrouped area. |
| `tab_id` | `str` | Optional | References a tab inside the tile's container by id. Requires containerId to be set, and the container to declare a matching tab. |
| `id` | `str` | Required | Unique tile ID assigned by the server. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_line_builder_chart_config import ClickStackLineBuilderChartConfig
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.click_stack_tile_output import ClickStackTileOutput
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_tile_output = ClickStackTileOutput(
    name='Error Rate',
    x=0,
    y=0,
    w=6,
    h=3,
    id='65f5e4a3b9e77c001a901234',
    config=ClickStackLineBuilderChartConfig(
        source_id='sourceId0',
        select=[
            ClickStackSelectItem(
                agg_fn=AggFn3.MAX,
                value_expression='valueExpression0',
                alias='alias4',
                level=Level.P50,
                where='where6',
                where_language=WhereLanguage4.SQL,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        group_by='groupBy4',
        as_ratio=False,
        align_date_range_to_granularity=False,
        fill_nulls=False,
        fit_y_axis_to_data=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    container_id='service-health',
    tab_id='errors',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

