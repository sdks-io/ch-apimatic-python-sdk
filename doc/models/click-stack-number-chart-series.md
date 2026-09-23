
# Click Stack Number Chart Series

*This model accepts additional fields of type Any.*

## Structure

`ClickStackNumberChartSeries`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required, Constant | Series type discriminator. Must be "number" for single-value number charts.<br><br>**Value**: `"number"` |
| `source_id` | `str` | Required | ID of the data source to query |
| `agg_fn` | [`AggFn`](../../doc/models/agg-fn.md) | Required | Aggregation function to apply to the field or metric value |
| `level` | `float` | Optional | Percentile level for quantile aggregations (e.g., 0.95 for p95) |
| `field` | `str` | Optional | Column or expression to aggregate (required for most aggregation functions except count) |
| `alias` | `str` | Optional | Display name for the series in the chart |
| `where` | `str` | Required | Filter query for the data (syntax depends on whereLanguage) |
| `where_language` | [`WhereLanguage`](../../doc/models/where-language.md) | Required | Query language for the where clause |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `metric_data_type` | [`MetricDataType`](../../doc/models/metric-data-type.md) | Optional | Metric data type, only for metrics data sources. |
| `metric_name` | `str` | Optional | Metric name for metrics data sources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn import AggFn
from openapispecforclickhousecloud.models.click_stack_number_chart_series import ClickStackNumberChartSeries
from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.metric_data_type import MetricDataType
from openapispecforclickhousecloud.models.output import Output
from openapispecforclickhousecloud.models.where_language import WhereLanguage

click_stack_number_chart_series = ClickStackNumberChartSeries(
    source_id='65f5e4a3b9e77c001a567890',
    agg_fn=AggFn.COUNT,
    where='service:api',
    where_language=WhereLanguage.LUCENE,
    level=0.95,
    field='duration',
    alias='Total Requests',
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
    metric_data_type=MetricDataType.SUM,
    metric_name='http.server.duration',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

