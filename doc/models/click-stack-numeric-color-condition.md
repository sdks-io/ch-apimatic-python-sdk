
# Click Stack Numeric Color Condition

*This model accepts additional fields of type Any.*

## Structure

`ClickStackNumericColorCondition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operator` | [`Operator`](../../doc/models/operator.md) | Required | Numeric comparison operator. |
| `value` | `float` | Required | Numeric bound the displayed value is compared against. Only finite numbers are accepted (Infinity and NaN are rejected). |
| `color` | [`Color1`](../../doc/models/color-1.md) | Required | Color applied when the rule matches. |
| `label` | `str` | Optional | Optional label describing the rule. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_numeric_color_condition import ClickStackNumericColorCondition
from openapispecforclickhousecloud.models.color_1 import Color1
from openapispecforclickhousecloud.models.operator import Operator

click_stack_numeric_color_condition = ClickStackNumericColorCondition(
    operator=Operator.GT,
    value=100,
    color=Color1.CHARTRED,
    label='High',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

