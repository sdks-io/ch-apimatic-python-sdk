
# Click Stack Aggregated Column

*This model accepts additional fields of type Any.*

## Structure

`ClickStackAggregatedColumn`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_column` | `str` | Optional | Source column name |
| `agg_fn` | `str` | Required | Aggregation function (e.g., count, sum, avg) |
| `mv_column` | `str` | Required | Materialized view column name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_aggregated_column import ClickStackAggregatedColumn

click_stack_aggregated_column = ClickStackAggregatedColumn(
    agg_fn='sum',
    mv_column='sum__Duration',
    source_column='Duration',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

