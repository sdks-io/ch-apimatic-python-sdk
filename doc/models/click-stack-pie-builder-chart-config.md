
# Click Stack Pie Builder Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackPieBuilderChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "pie" for pie charts.<br><br>**Value**: `"pie"` |
| `source_id` | `str` | Required | ID of the data source to query. |
| `select` | [`List[ClickStackSelectItem]`](../../doc/models/click-stack-select-item.md) | Required | Exactly one aggregated value used to size each pie slice. |
| `group_by` | `str` | Optional | Field expression to group results by (one slice per group value). |
| `order_by` | `str` | Optional | Optional custom SQL ORDER BY expression (raw SQL). Overrides the default value-descending ordering and, when combined with "limit", controls which slices are kept. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `limit` | `int` | Optional | Maximum number of slices (SQL LIMIT). Without a custom "orderBy" the query keeps the groups with the largest aggregated values; with an "orderBy" it keeps the first slices in that order. Omit or set 0 to fetch all groups. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.click_stack_pie_builder_chart_config import ClickStackPieBuilderChartConfig
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.output import Output
from openapispecforclickhousecloud.models.period_agg_fn import PeriodAggFn
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_pie_builder_chart_config = ClickStackPieBuilderChartConfig(
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
    order_by='"Count" DESC',
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
    limit=10,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

