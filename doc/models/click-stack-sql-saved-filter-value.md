
# Click Stack Sql Saved Filter Value

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSqlSavedFilterValue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type18`](../../doc/models/type-18.md) | Optional | Filter type. |
| `condition` | `str` | Required | SQL filter condition. For example use expressions in the form "column IN ('value')". |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_sql_saved_filter_value import ClickStackSqlSavedFilterValue
from openapispecforclickhousecloud.models.type_18 import Type18

click_stack_sql_saved_filter_value = ClickStackSqlSavedFilterValue(
    condition='ServiceName IN (\'hdx-oss-dev-api\')',
    mtype=Type18.SQL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

