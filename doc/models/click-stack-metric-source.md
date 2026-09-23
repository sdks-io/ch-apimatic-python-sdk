
# Click Stack Metric Source

*This model accepts additional fields of type Any.*

## Structure

`ClickStackMetricSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique source ID. Server-generated; ignored if sent in create/update requests. |
| `name` | `str` | Required | Display name for the source. |
| `section` | `str` | Optional | Optional grouping label used to organize sources in the source selector. Sources that share a section value are displayed together. |
| `disabled` | `bool` | Optional | When true, the source is hidden from source selectors in the UI. Defaults to false. |
| `kind` | `str` | Required, Constant | Source kind discriminator. Must be "metric" for metric sources.<br><br>**Value**: `"metric"` |
| `connection` | `str` | Required | ID of the ClickHouse connection used by this source. |
| `mfrom` | [`ClickStackMetricSourceFrom`](../../doc/models/click-stack-metric-source-from.md) | Required | - |
| `query_settings` | [`List[ClickStackQuerySetting]`](../../doc/models/click-stack-query-setting.md) | Optional | Optional ClickHouse query settings applied when querying this source. |
| `metric_tables` | [`ClickStackMetricTables`](../../doc/models/click-stack-metric-tables.md) | Required | - |
| `timestamp_value_expression` | `str` | Required | DateTime column or expression that is part of your table's primary key. |
| `resource_attributes_expression` | `str` | Required | Column containing resource attributes for metrics |
| `log_source_id` | `str` | Optional | HyperDX Source for logs associated with metrics. Optional |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_metric_source import ClickStackMetricSource
from openapispecforclickhousecloud.models.click_stack_metric_source_from import ClickStackMetricSourceFrom
from openapispecforclickhousecloud.models.click_stack_metric_tables import ClickStackMetricTables
from openapispecforclickhousecloud.models.click_stack_query_setting import ClickStackQuerySetting

click_stack_metric_source = ClickStackMetricSource(
    name='Metrics',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackMetricSourceFrom(
        database_name='otel',
        table_name='otel_metrics_gauge',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    metric_tables=ClickStackMetricTables(
        gauge='otel_metrics_gauge',
        histogram='otel_metrics_histogram',
        sum='otel_metrics_sum',
        summary='otel_metrics_summary',
        exponential_histogram='otel_metrics_exponential_histogram',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    timestamp_value_expression='TimeUnix',
    resource_attributes_expression='ResourceAttributes',
    id='507f1f77bcf86cd799439041',
    section='Billing',
    disabled=False,
    query_settings=[
        ClickStackQuerySetting(
            setting='setting6',
            value='value0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackQuerySetting(
            setting='setting6',
            value='value0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    log_source_id='507f1f77bcf86cd799439011',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

