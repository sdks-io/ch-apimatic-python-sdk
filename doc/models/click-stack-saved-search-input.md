
# Click Stack Saved Search Input

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSavedSearchInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Display name for the saved search. |
| `source_id` | `str` | Required | ID of the source to query. Must belong to the team. |
| `select` | `str` | Optional | Comma-separated list of column expressions to display. Empty uses the source default. |
| `where` | `str` | Optional | Row filter expression. The language is controlled by whereLanguage. |
| `where_language` | [`WhereLanguage12`](../../doc/models/where-language-12.md) | Optional | Language used for the where filter. |
| `order_by` | `str` | Optional | ORDER BY expression. Empty uses the source default. |
| `tags` | `List[str]` | Optional | Tags used to organize saved searches. |
| `filters` | [`List[ClickStackSavedSearchFilter]`](../../doc/models/click-stack-saved-search-filter.md) | Optional | Structured pinned filters applied to the search. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_saved_search_input import ClickStackSavedSearchInput
from openapispecforclickhousecloud.models.where_language_12 import WhereLanguage12

click_stack_saved_search_input = ClickStackSavedSearchInput(
    name='Production Errors',
    source_id='507f1f77bcf86cd799439012',
    select='Timestamp, ServiceName, Body',
    where='SeverityText:ERROR',
    where_language=WhereLanguage12.LUCENE,
    order_by='Timestamp DESC',
    tags=[
        'production',
        'errors'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

