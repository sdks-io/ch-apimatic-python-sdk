
# Click Stack Saved Search

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSavedSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique saved search ID. Server-generated. |
| `name` | `str` | Required | Display name for the saved search. |
| `source_id` | `str` | Required | ID of the source this saved search queries. |
| `select` | `str` | Optional | Comma-separated list of column expressions to display. Empty uses the source default. |
| `where` | `str` | Optional | Row filter expression. The language is controlled by whereLanguage. |
| `where_language` | [`WhereLanguage12`](../../doc/models/where-language-12.md) | Optional | Language used for the where filter. |
| `order_by` | `str` | Optional | ORDER BY expression. Empty uses the source default. |
| `tags` | `List[str]` | Optional | Tags used to organize saved searches. |
| `filters` | [`List[ClickStackSavedSearchFilter]`](../../doc/models/click-stack-saved-search-filter.md) | Optional | Structured pinned filters applied to the search. |
| `team_id` | `str` | Optional | ID of the team that owns the saved search. |
| `created_at` | `datetime` | Optional | Creation timestamp. |
| `updated_at` | `datetime` | Optional | Last update timestamp. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_saved_search import ClickStackSavedSearch
from openapispecforclickhousecloud.models.where_language_12 import WhereLanguage12

click_stack_saved_search = ClickStackSavedSearch(
    id='507f1f77bcf86cd799439011',
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
    team_id='507f1f77bcf86cd799439013',
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

