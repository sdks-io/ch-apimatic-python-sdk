
# Click Stack Line Raw Sql Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackLineRawSqlChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `config_type` | `str` | Required, Constant | Must be "sql" to use the Raw SQL chart config variant.<br><br>**Value**: `"sql"` |
| `connection_id` | `str` | Required | ID of the ClickHouse connection to execute the query against. |
| `sql_template` | `str` | Required | SQL query template to execute. Supports HyperDX template variables. |
| `source_id` | `str` | Optional | Optional ID of the data source associated with this Raw SQL chart. Used for applying dashboard filters. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `display_type` | `str` | Required, Constant | Display as a line time-series chart.<br><br>**Value**: `"line"` |
| `compare_to_previous_period` | `bool` | Optional | Overlay the equivalent previous time period for comparison. |
| `fill_nulls` | `bool` | Optional | Fill missing time buckets with zero instead of leaving gaps. |
| `align_date_range_to_granularity` | `bool` | Optional | Expand date range boundaries to the query granularity interval. |
| `fit_y_axis_to_data` | `bool` | Optional | Set the y-axis lower bound to the minimum of the displayed data instead of zero, making small fluctuations between series easier to see. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_line_raw_sql_chart_config import ClickStackLineRawSqlChartConfig
from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.output import Output

click_stack_line_raw_sql_chart_config = ClickStackLineRawSqlChartConfig(
    connection_id='65f5e4a3b9e77c001a567890',
    sql_template='SELECT count() FROM otel_logs WHERE timestamp > now() - INTERVAL 1 HOUR',
    source_id='65f5e4a3b9e77c001a567890',
    number_format=ClickStackNumberFormat(
        output=Output.CURRENCY,
        mantissa=170,
        thousand_separated=False,
        average=False,
        decimal_bytes=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    compare_to_previous_period=False,
    fill_nulls=False,
    align_date_range_to_granularity=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

