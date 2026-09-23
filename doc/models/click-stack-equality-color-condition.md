
# Click Stack Equality Color Condition

*This model accepts additional fields of type Any.*

## Structure

`ClickStackEqualityColorCondition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operator` | [`Operator1`](../../doc/models/operator-1.md) | Required | Equality comparison operator. |
| `value` | float \| str | Required | This is a container for one-of cases. |
| `color` | [`Color1`](../../doc/models/color-1.md) | Required | Color applied when the rule matches. |
| `label` | `str` | Optional | Optional label describing the rule. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_equality_color_condition import ClickStackEqualityColorCondition
from openapispecforclickhousecloud.models.color_1 import Color1
from openapispecforclickhousecloud.models.operator_1 import Operator1

click_stack_equality_color_condition = ClickStackEqualityColorCondition(
    operator=Operator1.EQ,
    value=138,
    color=Color1.CHARTLIGHTBLUE,
    label='Healthy',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

