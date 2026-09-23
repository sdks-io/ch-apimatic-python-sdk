
# Credit Balance

*This model accepts additional fields of type Any.*

## Structure

`CreditBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique ID of the balance. |
| `mtype` | [`Type21`](../../doc/models/type-21.md) | Optional | Type of the balance. |
| `remaining_credits` | `float` | Optional | Remaining credits available on this balance, in ClickHouse Credits (CHCs). |
| `total_amount` | `float` | Optional | Total credits granted on this balance, in ClickHouse Credits (CHCs). |
| `amount_spent` | `float` | Optional | Credits spent from this balance, in ClickHouse Credits (CHCs). |
| `start_date` | `datetime` | Optional | Date the balance became active. ISO-8601, based on the UTC timezone. |
| `expiration_date` | `datetime` | Optional | Date the balance expires. ISO-8601, based on the UTC timezone. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.credit_balance import CreditBalance
from openapispecforclickhousecloud.models.type_21 import Type21

credit_balance = CreditBalance(
    id='00001f4e-0000-0000-0000-000000000000',
    mtype=Type21.PREPAID,
    remaining_credits=74.48,
    total_amount=244.98,
    amount_spent=104.36,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

