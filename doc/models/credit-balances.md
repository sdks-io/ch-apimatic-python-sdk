
# Credit Balances

*This model accepts additional fields of type Any.*

## Structure

`CreditBalances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_remaining_credits` | `float` | Optional | Total remaining credits across all active balances, in ClickHouse Credits (CHCs). |
| `balances` | [`List[CreditBalance]`](../../doc/models/credit-balance.md) | Optional | List of active balances for the organization. Empty when the organization has none. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.credit_balance import CreditBalance
from openapispecforclickhousecloud.models.credit_balances import CreditBalances
from openapispecforclickhousecloud.models.type_21 import Type21

credit_balances = CreditBalances(
    total_remaining_credits=79.64,
    balances=[
        CreditBalance(
            id='000008c0-0000-0000-0000-000000000000',
            mtype=Type21.PREPAID,
            remaining_credits=172.74,
            total_amount=87.24,
            amount_spent=202.62,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CreditBalance(
            id='000008c0-0000-0000-0000-000000000000',
            mtype=Type21.PREPAID,
            remaining_credits=172.74,
            total_amount=87.24,
            amount_spent=202.62,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CreditBalance(
            id='000008c0-0000-0000-0000-000000000000',
            mtype=Type21.PREPAID,
            remaining_credits=172.74,
            total_amount=87.24,
            amount_spent=202.62,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

