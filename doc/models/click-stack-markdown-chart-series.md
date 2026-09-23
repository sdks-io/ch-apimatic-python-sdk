
# Click Stack Markdown Chart Series

*This model accepts additional fields of type Any.*

## Structure

`ClickStackMarkdownChartSeries`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required, Constant | Series type discriminator. Must be "markdown" for markdown text widgets.<br><br>**Value**: `"markdown"` |
| `content` | `str` | Required | Markdown content to render inside the widget. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_markdown_chart_series import ClickStackMarkdownChartSeries

click_stack_markdown_chart_series = ClickStackMarkdownChartSeries(
    content='# Dashboard Title\n\nThis is a markdown widget.',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

