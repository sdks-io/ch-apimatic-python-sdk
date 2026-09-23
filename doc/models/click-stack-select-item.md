
# Click Stack Select Item

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSelectItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agg_fn` | [`AggFn3`](../../doc/models/agg-fn-3.md) | Required | Aggregation function to apply. "count" does not require a valueExpression; "quantile" requires a level field indicating the desired percentile (e.g., 0.95). |
| `value_expression` | `str` | Optional | Expression for the column or value to aggregate. Must be omitted when aggFn is "count"; required for all other aggFn values. |
| `alias` | `str` | Optional | Display alias for this select item in chart legends. |
| `level` | [`Level`](../../doc/models/level.md) | Optional | Percentile level; only valid when aggFn is "quantile". |
| `where` | `str` | Optional | SQL or Lucene filter condition applied before aggregation. |
| `where_language` | [`WhereLanguage4`](../../doc/models/where-language-4.md) | Optional | Query language for the where clause. |
| `metric_name` | `str` | Optional | Name of the metric to aggregate; only applicable when the source is a metrics source. |
| `metric_type` | [`MetricType`](../../doc/models/metric-type.md) | Optional | Metric type; only applicable when the source is a metrics source. |
| `period_agg_fn` | [`PeriodAggFn`](../../doc/models/period-agg-fn.md) | Optional | Optional period aggregation function for Gauge metrics (e.g., compute the delta over the period). |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.period_agg_fn import PeriodAggFn
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_select_item = ClickStackSelectItem(
    agg_fn=AggFn3.COUNT,
    value_expression='Duration',
    alias='Request Duration',
    level=Level.P95,
    where='service:api',
    where_language=WhereLanguage4.SQL,
    metric_name='http.server.duration',
    period_agg_fn=PeriodAggFn.DELTA,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

