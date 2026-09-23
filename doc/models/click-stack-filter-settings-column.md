
# Click Stack Filter Settings Column

*This model accepts additional fields of type Any.*

## Structure

`ClickStackFilterSettingsColumn`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Column of the source's table that selected filter values are matched against. Also the key the selection is persisted under in links, saved searches, and dashboards. |
| `label` | `str` | Required | Display label for the column |
| `value_expression` | `str` | Optional | Optional SQL expression, evaluated against the filter-values table, that produces the available filter options. Use it when the options live in a differently-named column, or must be transformed to match the values stored in the source table. Defaults to reading `name` as a plain column when omitted. |
| `allow_all` | `bool` | Optional | Whether to offer an "All" option that expands to every available value at query time. Best suited to low-cardinality columns. Defaults to false. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_filter_settings_column import ClickStackFilterSettingsColumn

click_stack_filter_settings_column = ClickStackFilterSettingsColumn(
    name='ServiceName',
    label='Service Name',
    value_expression='lower(service_name)',
    allow_all=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

