
# Click Stack Source Filter Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSourceFilterSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `database_name` | `str` | Required | ClickHouse database name |
| `table_name` | `str` | Required | ClickHouse table name |
| `columns` | [`List[ClickStackFilterSettingsColumn]`](../../doc/models/click-stack-filter-settings-column.md) | Required | Columns to expose as filters (max 10) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_filter_settings_column import ClickStackFilterSettingsColumn
from openapispecforclickhousecloud.models.click_stack_source_filter_settings import ClickStackSourceFilterSettings

click_stack_source_filter_settings = ClickStackSourceFilterSettings(
    database_name='default',
    table_name='otel_logs',
    columns=[
        ClickStackFilterSettingsColumn(
            name='ServiceName',
            label='Service Name',
            value_expression='lower(service_name)',
            allow_all=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

