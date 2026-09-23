
# Click Stack Number Format

*This model accepts additional fields of type Any.*

## Structure

`ClickStackNumberFormat`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `output` | [`Output`](../../doc/models/output.md) | Optional | Output format applied to the number. |
| `mantissa` | `int` | Optional | Number of decimal places. |
| `thousand_separated` | `bool` | Optional | Whether to use thousand separators. |
| `average` | `bool` | Optional | Whether to show as average. |
| `decimal_bytes` | `bool` | Optional | Use decimal bytes (1000) vs binary bytes (1024). |
| `factor` | `float` | Optional | Multiplication factor. |
| `currency_symbol` | `str` | Optional | Currency symbol for currency format. |
| `numeric_unit` | [`NumericUnit`](../../doc/models/numeric-unit.md) | Optional | Numeric unit for data, data rate, or throughput formats. |
| `unit` | `str` | Optional | Custom unit label. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.numeric_unit import NumericUnit
from openapispecforclickhousecloud.models.output import Output

click_stack_number_format = ClickStackNumberFormat(
    output=Output.NUMBER,
    mantissa=2,
    thousand_separated=True,
    average=False,
    decimal_bytes=False,
    factor=1,
    currency_symbol='$',
    numeric_unit=NumericUnit.BYTES_IEC,
    unit='ms',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

