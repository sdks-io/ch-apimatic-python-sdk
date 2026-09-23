
# Prometheus Discovery Labels

*This model accepts additional fields of type Any.*

## Structure

`PrometheusDiscoveryLabels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme` | `str` | Optional | URL scheme Prometheus must scrape the target with. |
| `metrics_path` | `str` | Optional | Path of the per-service Prometheus metrics endpoint. |
| `param_filtered_metrics` | `str` | Optional | Value passed as the filtered_metrics query parameter on each scrape. |
| `clickhouse_org_id` | `uuid\|str` | Optional | Organization ID the service belongs to. |
| `clickhouse_service_id` | `uuid\|str` | Optional | Service ID. |
| `clickhouse_discovery_service_name` | `str` | Optional | Service name. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.prometheus_discovery_labels import PrometheusDiscoveryLabels

prometheus_discovery_labels = PrometheusDiscoveryLabels(
    scheme='__scheme__4',
    metrics_path='__metrics_path__8',
    param_filtered_metrics='__param_filtered_metrics4',
    clickhouse_org_id='00000c8c-0000-0000-0000-000000000000',
    clickhouse_service_id='000012fa-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

