
# Click Stack Metric Source From

*This model accepts additional fields of type Any.*

## Structure

`ClickStackMetricSourceFrom`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `database_name` | `str` | Required | ClickHouse database name |
| `table_name` | `str` | Optional | ClickHouse table name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_metric_source_from import ClickStackMetricSourceFrom

click_stack_metric_source_from = ClickStackMetricSourceFrom(
    database_name='otel',
    table_name='otel_metrics_gauge',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

