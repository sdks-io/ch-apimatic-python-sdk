
# Click Stack Query Setting

*This model accepts additional fields of type Any.*

## Structure

`ClickStackQuerySetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `setting` | `str` | Required | ClickHouse setting name |
| `value` | `str` | Required | Setting value |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_query_setting import ClickStackQuerySetting

click_stack_query_setting = ClickStackQuerySetting(
    setting='max_threads',
    value='4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

