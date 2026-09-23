
# Postgres Metric Series

*This model accepts additional fields of type Any.*

## Structure

`PostgresMetricSeries`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `label` | `str` | Required | Distinguishing label for this series within the metric (for example a CPU mode, a database name, or "Reads"). |
| `data_points` | [`List[PostgresMetricDataPoint]`](../../doc/models/postgres-metric-data-point.md) | Required | Time-ordered data points, one per bucket. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_metric_data_point import PostgresMetricDataPoint
from openapispecforclickhousecloud.models.postgres_metric_series import PostgresMetricSeries

postgres_metric_series = PostgresMetricSeries(
    label='label4',
    data_points=[
        PostgresMetricDataPoint(
            timestamp=4,
            value=27.1,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

