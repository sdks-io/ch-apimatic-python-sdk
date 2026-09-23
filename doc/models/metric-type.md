
# Metric Type

Metric type; only applicable when the source is a metrics source.

## Enumeration

`MetricType`

## Fields

| Name |
|  --- |
| `SUM` |
| `GAUGE` |
| `HISTOGRAM` |
| `SUMMARY` |
| `ENUM_EXPONENTIAL_HISTOGRAM` |

## Example

```python
from openapispecforclickhousecloud.models.metric_type import MetricType

metric_type = MetricType.ENUM_EXPONENTIAL_HISTOGRAM
```

