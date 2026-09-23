
# Click Stack Markdown Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackMarkdownChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "markdown" for markdown text tiles.<br><br>**Value**: `"markdown"` |
| `markdown` | `str` | Optional | Markdown content to render inside the tile. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_markdown_chart_config import ClickStackMarkdownChartConfig

click_stack_markdown_chart_config = ClickStackMarkdownChartConfig(
    markdown='# Dashboard Title\n\nThis is a markdown widget.',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

