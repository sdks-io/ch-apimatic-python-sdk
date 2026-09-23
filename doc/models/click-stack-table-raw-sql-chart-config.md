
# Click Stack Table Raw Sql Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackTableRawSqlChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `config_type` | `str` | Required, Constant | Must be "sql" to use the Raw SQL chart config variant.<br><br>**Value**: `"sql"` |
| `connection_id` | `str` | Required | ID of the ClickHouse connection to execute the query against. |
| `sql_template` | `str` | Required | SQL query template to execute. Supports HyperDX template variables. |
| `source_id` | `str` | Optional | Optional ID of the data source associated with this Raw SQL chart. Used for applying dashboard filters. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `display_type` | `str` | Required, Constant | Display as a table chart.<br><br>**Value**: `"table"` |
| `on_click` | [ClickStackOnClickSearch](../../doc/models/click-stack-on-click-search.md) \| [ClickStackOnClickDashboard](../../doc/models/click-stack-on-click-dashboard.md) \| [ClickStackOnClickExternal](../../doc/models/click-stack-on-click-external.md) \| None | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.click_stack_on_click_filter_template import ClickStackOnClickFilterTemplate
from openapispecforclickhousecloud.models.click_stack_on_click_search import ClickStackOnClickSearch
from openapispecforclickhousecloud.models.click_stack_on_click_target_id_variant import ClickStackOnClickTargetIdVariant
from openapispecforclickhousecloud.models.click_stack_table_raw_sql_chart_config import ClickStackTableRawSqlChartConfig
from openapispecforclickhousecloud.models.output import Output
from openapispecforclickhousecloud.models.where_language_5 import WhereLanguage5

click_stack_table_raw_sql_chart_config = ClickStackTableRawSqlChartConfig(
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
    on_click=ClickStackOnClickSearch(
        target=ClickStackOnClickTargetIdVariant(
            id='id0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        where_template='whereTemplate8',
        where_language=WhereLanguage5.SQL,
        filters=[
            ClickStackOnClickFilterTemplate(
                expression='expression2',
                template='template4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ClickStackOnClickFilterTemplate(
                expression='expression2',
                template='template4',
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

