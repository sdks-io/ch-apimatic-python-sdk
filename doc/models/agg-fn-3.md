
# Agg Fn 3

Aggregation function to apply. "count" does not require a valueExpression; "quantile" requires a level field indicating the desired percentile (e.g., 0.95).

## Enumeration

`AggFn3`

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
from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3

agg_fn_3 = AggFn3.MAX
```

