
# Click Stack Saved Search Filter

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSavedSearchFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type20`](../../doc/models/type-20.md) | Optional | Always `sql`. Only SQL predicate filters render in the sidebar. |
| `condition` | `str` | Required | SQL predicate applied to the search, in `<column> IN (...)` form. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_saved_search_filter import ClickStackSavedSearchFilter
from openapispecforclickhousecloud.models.type_20 import Type20

click_stack_saved_search_filter = ClickStackSavedSearchFilter(
    condition='ServiceName IN (\'checkout\', \'payments\')',
    mtype=Type20.SQL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

