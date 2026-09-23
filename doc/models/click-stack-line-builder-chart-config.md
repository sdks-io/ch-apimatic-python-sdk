
# Click Stack Line Builder Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackLineBuilderChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "line" for line charts.<br><br>**Value**: `"line"` |
| `source_id` | `str` | Required | ID of the data source to query. |
| `select` | [`List[ClickStackSelectItem]`](../../doc/models/click-stack-select-item.md) | Required | One or more aggregated values to plot. When asRatio is true, exactly two select items are required. |
| `group_by` | `str` | Optional | Field expression to group results by (creates separate lines per group value). |
| `as_ratio` | `bool` | Optional | Plot select[0] / select[1] as a ratio. Requires exactly two select items. |
| `align_date_range_to_granularity` | `bool` | Optional | Expand date range boundaries to the query granularity interval. |
| `fill_nulls` | `bool` | Optional | Fill missing time buckets with zero instead of leaving gaps. |
| `fit_y_axis_to_data` | `bool` | Optional | Set the y-axis lower bound to the minimum of the displayed data instead of zero, making small fluctuations between series easier to see. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `compare_to_previous_period` | `bool` | Optional | Overlay the equivalent previous time period for comparison. |
| `series_limit` | `int` | Optional | Maximum number of series rendered (top-N by value). Omit to use the default render cap, set 0 for unlimited, or a positive N to keep the top N series. |
| `formulas` | [`List[ClickStackFormula]`](../../doc/models/click-stack-formula.md) | Optional | Derived series computed from the select items via letter-ref arithmetic ("A" = select[0], "B" = select[1], ...). Metric, log, and trace sources only. Cannot be combined with asRatio. |
| `show_operand_series` | `bool` | Optional | Only meaningful with formulas. When false, only the formula series are returned; the raw operand series are hidden. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_line_builder_chart_config import ClickStackLineBuilderChartConfig
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.period_agg_fn import PeriodAggFn
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_line_builder_chart_config = ClickStackLineBuilderChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.COUNT,
            value_expression='Duration',
            alias='Request Duration',
            level=Level.P50,
            where='service:api',
            where_language=WhereLanguage4.SQL,
            metric_name='http.server.duration',
            period_agg_fn=PeriodAggFn.DELTA,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    group_by='host',
    as_ratio=False,
    align_date_range_to_granularity=False,
    fill_nulls=False,
    fit_y_axis_to_data=False,
    series_limit=5,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

