
# V1 Organizations Postgres Metrics Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresMetricsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`PostgresMetrics`](../../doc/models/postgres-metrics.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_metric import PostgresMetric
from openapispecforclickhousecloud.models.postgres_metric_data_point import PostgresMetricDataPoint
from openapispecforclickhousecloud.models.postgres_metric_series import PostgresMetricSeries
from openapispecforclickhousecloud.models.postgres_metrics import PostgresMetrics
from openapispecforclickhousecloud.models.v_1_organizations_postgres_metrics_response import V1OrganizationsPostgresMetricsResponse

v_1_organizations_postgres_metrics_response = V1OrganizationsPostgresMetricsResponse(
    status=200,
    request_id='000024f2-0000-0000-0000-000000000000',
    result=PostgresMetrics(
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
                            ),
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
                    ),
                    PostgresMetricSeries(
                        label='label4',
                        data_points=[
                            PostgresMetricDataPoint(
                                timestamp=4,
                                value=27.1,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
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
                    ),
                    PostgresMetricSeries(
                        label='label4',
                        data_points=[
                            PostgresMetricDataPoint(
                                timestamp=4,
                                value=27.1,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
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
            ),
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
                            ),
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
                    ),
                    PostgresMetricSeries(
                        label='label4',
                        data_points=[
                            PostgresMetricDataPoint(
                                timestamp=4,
                                value=27.1,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
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
                    ),
                    PostgresMetricSeries(
                        label='label4',
                        data_points=[
                            PostgresMetricDataPoint(
                                timestamp=4,
                                value=27.1,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

