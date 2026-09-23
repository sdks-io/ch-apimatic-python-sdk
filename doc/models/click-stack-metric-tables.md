
# Click Stack Metric Tables

*This model accepts additional fields of type Any.*

## Structure

`ClickStackMetricTables`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gauge` | `str` | Optional | Table containing gauge metrics data |
| `histogram` | `str` | Optional | Table containing histogram metrics data |
| `sum` | `str` | Optional | Table containing sum metrics data |
| `summary` | `str` | Optional | Table containing summary metrics data. Note - not yet fully supported by HyperDX |
| `exponential_histogram` | `str` | Optional | Table containing exponential histogram metrics data. Note - not yet fully supported by HyperDX |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_metric_tables import ClickStackMetricTables

click_stack_metric_tables = ClickStackMetricTables(
    gauge='otel_metrics_gauge',
    histogram='otel_metrics_histogram',
    sum='otel_metrics_sum',
    summary='otel_metrics_summary',
    exponential_histogram='otel_metrics_exponential_histogram',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

