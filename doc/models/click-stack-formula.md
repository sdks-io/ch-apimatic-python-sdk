
# Click Stack Formula

*This model accepts additional fields of type Any.*

## Structure

`ClickStackFormula`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expression` | `str` | Required | Arithmetic expression over the select items by position, e.g. "A / (A + B) * 100" for a success-rate percentage. |
| `alias` | `str` | Optional | Display label for the formula series in chart legends and column headers. Falls back to the raw expression text when unset. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_formula import ClickStackFormula
from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.output import Output

click_stack_formula = ClickStackFormula(
    expression='A / (A + B) * 100',
    alias='Success rate %',
    number_format=ClickStackNumberFormat(
        output=Output.CURRENCY,
        mantissa=170,
        thousand_separated=False,
        average=False,
        decimal_bytes=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

