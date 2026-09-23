
# Click Stack Materialized View

*This model accepts additional fields of type Any.*

## Structure

`ClickStackMaterializedView`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `database_name` | `str` | Required | Database name for the materialized view |
| `table_name` | `str` | Required | Table name for the materialized view |
| `dimension_columns` | `str` | Required | Columns which are not pre-aggregated in the materialized view and can be used for filtering and grouping. |
| `min_granularity` | `str` | Required | The granularity of the timestamp column: a positive integer followed by a unit (s, m, h, d). Common values: 1s, 15s, 30s, 1m, 5m, 15m, 30m, 1h, 2h, 6h, 12h, 1d, 2d, 7d, 30d. |
| `min_date` | `datetime` | Optional | (Optional) The earliest date and time for which the materialized view contains data. If not provided, then HyperDX will assume that the materialized view contains data for all dates for which the source table contains data. |
| `timestamp_column` | `str` | Required | Timestamp column name |
| `aggregated_columns` | [`List[ClickStackAggregatedColumn]`](../../doc/models/click-stack-aggregated-column.md) | Required | Columns which are pre-aggregated by the materialized view |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_aggregated_column import ClickStackAggregatedColumn
from openapispecforclickhousecloud.models.click_stack_materialized_view import ClickStackMaterializedView

click_stack_materialized_view = ClickStackMaterializedView(
    database_name='otel',
    table_name='otel_logs_mv_5m',
    dimension_columns='ServiceName, SeverityText',
    min_granularity='5m',
    timestamp_column='Timestamp',
    aggregated_columns=[
        ClickStackAggregatedColumn(
            agg_fn='sum',
            mv_column='sum__Duration',
            source_column='Duration',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    min_date=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

