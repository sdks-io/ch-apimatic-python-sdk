
# Agg Fn

Aggregation function to apply to the field or metric value

## Enumeration

`AggFn`

## Fields

| Name |
|  --- |
| `AVG` |
| `COUNT` |
| `COUNT_DISTINCT` |
| `LAST_VALUE` |
| `MAX` |
| `MIN` |
| `QUANTILE` |
| `SUM` |
| `ANY` |
| `NONE` |

## Example

```python
from openapispecforclickhousecloud.models.agg_fn import AggFn

agg_fn = AggFn.QUANTILE
```

