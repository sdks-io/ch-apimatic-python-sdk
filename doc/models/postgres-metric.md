
# Postgres Metric

*This model accepts additional fields of type Any.*

## Structure

`PostgresMetric`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | Stable metric identifier (for example cpu_usage, connection_count, cache_hit_ratio). |
| `name` | `str` | Required | Human-readable metric name. |
| `unit` | `str` | Required | Unit of the metric values (for example %, IOPS, bytes/s, count). |
| `description` | `str` | Required | Human-readable description of what the metric measures. |
| `series` | [`List[PostgresMetricSeries]`](../../doc/models/postgres-metric-series.md) | Required | One series per label dimension of the metric. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_metric import PostgresMetric
from openapispecforclickhousecloud.models.postgres_metric_data_point import PostgresMetricDataPoint
from openapispecforclickhousecloud.models.postgres_metric_series import PostgresMetricSeries

postgres_metric = PostgresMetric(
    key='key8',
    name='name8',
    unit='unit6',
    description='description8',
    series=[
        PostgresMetricSeries(
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

