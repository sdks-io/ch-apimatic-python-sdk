
# Click Stack Event Patterns Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackEventPatternsChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "event_patterns" for pattern mining tiles.<br><br>**Value**: `"event_patterns"` |
| `source_id` | `str` | Required | ID of the data source to mine patterns from. |
| `select` | `str` | Optional | Column or expression to mine patterns from. Leave empty to use the source default (Body for logs, SpanName for traces). |
| `where` | `str` | Optional | Filter condition for the pattern mining query (syntax depends on whereLanguage). |
| `where_language` | [`WhereLanguage4`](../../doc/models/where-language-4.md) | Optional | Query language for the where clause. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_event_patterns_chart_config import ClickStackEventPatternsChartConfig
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_event_patterns_chart_config = ClickStackEventPatternsChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select='Body',
    where='level:error',
    where_language=WhereLanguage4.SQL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

