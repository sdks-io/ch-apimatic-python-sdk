
# Postgres Metric Data Point

*This model accepts additional fields of type Any.*

## Structure

`PostgresMetricDataPoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `int` | Required | Bucket start time as a Unix timestamp in seconds. |
| `value` | `float` | Required | Metric value for the bucket. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_metric_data_point import PostgresMetricDataPoint

postgres_metric_data_point = PostgresMetricDataPoint(
    timestamp=10,
    value=42.32,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

