
# Click Stack Search Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSearchChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "search" for search/log viewer tiles.<br><br>**Value**: `"search"` |
| `source_id` | `str` | Required | ID of the data source to query. |
| `select` | `str` | Required | Comma-separated list of expressions to display. |
| `where` | `str` | Optional | Filter condition for the search (syntax depends on whereLanguage). |
| `where_language` | [`WhereLanguage4`](../../doc/models/where-language-4.md) | Required | Query language for the where clause. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_search_chart_config import ClickStackSearchChartConfig
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_search_chart_config = ClickStackSearchChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select='timestamp, level, message',
    where_language=WhereLanguage4.SQL,
    where='level:error',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

