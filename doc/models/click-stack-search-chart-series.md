
# Click Stack Search Chart Series

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSearchChartSeries`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required, Constant | Series type discriminator. Must be "search" for search/log viewer charts.<br><br>**Value**: `"search"` |
| `source_id` | `str` | Required | ID of the data source to query |
| `fields` | `List[str]` | Required | List of field names to display in the search results table |
| `where` | `str` | Required | Filter query for the data (syntax depends on whereLanguage) |
| `where_language` | [`WhereLanguage`](../../doc/models/where-language.md) | Required | Query language for the where clause |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_search_chart_series import ClickStackSearchChartSeries
from openapispecforclickhousecloud.models.where_language import WhereLanguage

click_stack_search_chart_series = ClickStackSearchChartSeries(
    source_id='65f5e4a3b9e77c001a567890',
    fields=[
        'timestamp',
        'level',
        'message'
    ],
    where='level:error',
    where_language=WhereLanguage.LUCENE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

