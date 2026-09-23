
# Postgres Metrics

*This model accepts additional fields of type Any.*

## Structure

`PostgresMetrics`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metrics` | [`List[PostgresMetric]`](../../doc/models/postgres-metric.md) | Required | Available metrics, each with its bucketed time series. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_metric import PostgresMetric
from openapispecforclickhousecloud.models.postgres_metric_data_point import PostgresMetricDataPoint
from openapispecforclickhousecloud.models.postgres_metric_series import PostgresMetricSeries
from openapispecforclickhousecloud.models.postgres_metrics import PostgresMetrics

postgres_metrics = PostgresMetrics(
    metrics=[
        PostgresMetric(
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

