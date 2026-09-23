
# Click Stack Highlighted Attribute Expression

*This model accepts additional fields of type Any.*

## Structure

`ClickStackHighlightedAttributeExpression`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sql_expression` | `str` | Required | SQL expression for the attribute |
| `lucene_expression` | `str` | Optional | An optional, Lucene version of the sqlExpression expression. If provided, it is used when searching for this attribute value. |
| `alias` | `str` | Optional | Optional alias for the attribute |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_highlighted_attribute_expression import ClickStackHighlightedAttributeExpression

click_stack_highlighted_attribute_expression = ClickStackHighlightedAttributeExpression(
    sql_expression='SpanAttributes[\'http.status_code\']',
    lucene_expression='http.status_code',
    alias='HTTP Status Code',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

