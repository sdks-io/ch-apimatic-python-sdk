
# Click Stack between Color Condition

*This model accepts additional fields of type Any.*

## Structure

`ClickStackBetweenColorCondition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operator` | `str` | Required, Constant | Range comparison operator.<br><br>**Value**: `"between"` |
| `value` | `List[float]` | Required | Inclusive [min, max] range. Both bounds must be finite numbers. |
| `color` | [`Color1`](../../doc/models/color-1.md) | Required | Color applied when the rule matches. |
| `label` | `str` | Optional | Optional label describing the rule. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_between_color_condition import ClickStackBetweenColorCondition
from openapispecforclickhousecloud.models.color_1 import Color1

click_stack_between_color_condition = ClickStackBetweenColorCondition(
    value=[
        100,
        500
    ],
    color=Color1.CHARTGREEN,
    label='Warning',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

