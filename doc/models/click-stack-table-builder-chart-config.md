
# Click Stack Table Builder Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackTableBuilderChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "table" for table charts.<br><br>**Value**: `"table"` |
| `source_id` | `str` | Required | ID of the data source to query. |
| `select` | [`List[ClickStackSelectItem]`](../../doc/models/click-stack-select-item.md) | Required | One or more aggregated values to display as table columns. When asRatio is true, exactly two select items are required. |
| `group_by` | `str` | Optional | Field expression to group results by (one row per group value). |
| `having` | `str` | Optional | Post-aggregation SQL HAVING condition. |
| `order_by` | `str` | Optional | SQL ORDER BY expression for sorting table rows. |
| `as_ratio` | `bool` | Optional | Display select[0] / select[1] as a ratio. Requires exactly two select items. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `group_by_columns_on_left` | `bool` | Optional | When true, render Group By columns to the left of series columns in the table. Defaults to false (Group By columns on the right). |
| `on_click` | [ClickStackOnClickSearch](../../doc/models/click-stack-on-click-search.md) \| [ClickStackOnClickDashboard](../../doc/models/click-stack-on-click-dashboard.md) \| [ClickStackOnClickExternal](../../doc/models/click-stack-on-click-external.md) \| None | Optional | - |
| `formulas` | [`List[ClickStackFormula]`](../../doc/models/click-stack-formula.md) | Optional | Derived columns computed from the select items via letter-ref arithmetic ("A" = select[0], "B" = select[1], ...). Metric, log, and trace sources only. Cannot be combined with asRatio. |
| `show_operand_series` | `bool` | Optional | Only meaningful with formulas. When false, only the formula columns are returned; the raw operand columns are hidden. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.click_stack_table_builder_chart_config import ClickStackTableBuilderChartConfig
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.output import Output
from openapispecforclickhousecloud.models.period_agg_fn import PeriodAggFn
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_table_builder_chart_config = ClickStackTableBuilderChartConfig(
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
    group_by='service',
    having='count > 100',
    order_by='count DESC',
    as_ratio=False,
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
    group_by_columns_on_left=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

