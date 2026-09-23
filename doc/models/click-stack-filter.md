
# Click Stack Filter

*This model accepts additional fields of type Any.*

## Structure

`ClickStackFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required, Constant | Filter type. Must be "QUERY_EXPRESSION".<br><br>**Value**: `"QUERY_EXPRESSION"` |
| `name` | `str` | Required | Display name for the dashboard filter key |
| `expression` | `str` | Required | SQL expression used when querying values for this filter, and when applying this dashboard filter to tiles. |
| `source_id` | `str` | Required | Source ID this dashboard filter key applies to |
| `source_metric_type` | [`SourceMetricType`](../../doc/models/source-metric-type.md) | Optional | Metric type when source is metrics |
| `where` | `str` | Optional | Optional WHERE condition to scope which rows this filter key reads values from |
| `where_language` | [`WhereLanguage10`](../../doc/models/where-language-10.md) | Optional | Language of the where condition |
| `applies_to_source_ids` | `List[str]` | Optional | Optional list of source IDs this filter applies to. Omit or provide an empty array to apply the filter to ALL tiles regardless of source. A non-empty array restricts the filter to only tiles whose source ID is in the list; tiles using other sources are not affected by the selected filter value(s). Scopes the broadcast condition only, so a non-empty array is rejected when isBroadcastEnabled is false, and is omitted from responses for such a filter. |
| `is_broadcast_enabled` | `bool` | Optional | Whether the selected value is applied as a filter condition on every builder tile this filter applies to (see appliesToSourceIds), and every raw sql tile using the $__filters macro. Omitting the field means enabled. |
| `is_variable_enabled` | `bool` | Optional | Whether the selected value is exposed to tile queries as a dashboard variable named by variableName. Tiles may reference it as `$variableName` or using the (preferred) `$__filter($<variableName>)` and `$__conditionalAll(<condition>, $<variableName>)` macros. |
| `variable_name` | `str` | Optional | Token tiles reference this filter's selected value by, as `$variableName`. Must start with a letter and may contain only letters, numbers, and underscores. Defaults to the display name with whitespace replaced by underscores and remaining illegal characters removed, so a variable-enabled filter whose name derives nothing usable must send this field explicitly. Variable names must be unique across a dashboard's variable-enabled filters. Names the variable only, so the field is rejected when isVariableEnabled is not true, and is omitted from responses for such a filter. |
| `id` | `str` | Required | Unique dashboard filter key ID |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_filter import ClickStackFilter
from openapispecforclickhousecloud.models.source_metric_type import SourceMetricType
from openapispecforclickhousecloud.models.where_language_10 import WhereLanguage10

click_stack_filter = ClickStackFilter(
    name='Environment',
    expression='environment',
    source_id='65f5e4a3b9e77c001a111111',
    id='id4',
    source_metric_type=SourceMetricType.GAUGE,
    where='ServiceName:api',
    where_language=WhereLanguage10.LUCENE,
    applies_to_source_ids=[
        '65f5e4a3b9e77c001a111111'
    ],
    is_broadcast_enabled=False,
    is_variable_enabled=True,
    variable_name='environment',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

