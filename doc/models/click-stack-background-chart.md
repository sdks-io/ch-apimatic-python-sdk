
# Click Stack Background Chart

*This model accepts additional fields of type Any.*

## Structure

`ClickStackBackgroundChart`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type19`](../../doc/models/type-19.md) | Required | Sparkline shape. |
| `color` | [`Color`](../../doc/models/color.md) | Optional | Optional palette-token override for the sparkline. When unset the sparkline inherits the tile's static color. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_background_chart import ClickStackBackgroundChart
from openapispecforclickhousecloud.models.color import Color
from openapispecforclickhousecloud.models.type_19 import Type19

click_stack_background_chart = ClickStackBackgroundChart(
    mtype=Type19.LINE,
    color=Color.CHARTORANGE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

