
# Prometheus Discovery Target Group

*This model accepts additional fields of type Any.*

## Structure

`PrometheusDiscoveryTargetGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `targets` | `List[str]` | Optional | Host (and port) of the ClickHouse Cloud API. |
| `labels` | [`PrometheusDiscoveryLabels`](../../doc/models/prometheus-discovery-labels.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.prometheus_discovery_labels import PrometheusDiscoveryLabels
from openapispecforclickhousecloud.models.prometheus_discovery_target_group import PrometheusDiscoveryTargetGroup

prometheus_discovery_target_group = PrometheusDiscoveryTargetGroup(
    targets=[
        'targets6',
        'targets7'
    ],
    labels=PrometheusDiscoveryLabels(
        scheme='__scheme__0',
        metrics_path='__metrics_path__4',
        param_filtered_metrics='__param_filtered_metrics0',
        clickhouse_org_id='000026d0-0000-0000-0000-000000000000',
        clickhouse_service_id='0000074a-0000-0000-0000-000000000000',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

