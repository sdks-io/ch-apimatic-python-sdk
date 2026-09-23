
# Click Stack Source From

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSourceFrom`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `database_name` | `str` | Required | ClickHouse database name |
| `table_name` | `str` | Required | ClickHouse table name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_source_from import ClickStackSourceFrom

click_stack_source_from = ClickStackSourceFrom(
    database_name='otel',
    table_name='otel_logs',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

