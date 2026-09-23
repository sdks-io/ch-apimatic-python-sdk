
# Active Balances

*This model accepts additional fields of type Any.*

## Structure

`ActiveBalances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_remaining_prepaid_credits` | `float` | Optional | Total remaining credits across all active prepaid balances, in ClickHouse Credits (CHCs). |
| `prepaid_balances` | [`List[ActiveBalance]`](../../doc/models/active-balance.md) | Optional | List of active prepaid balances for the organization. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.active_balance import ActiveBalance
from openapispecforclickhousecloud.models.active_balances import ActiveBalances

active_balances = ActiveBalances(
    total_remaining_prepaid_credits=98.24,
    prepaid_balances=[
        ActiveBalance(
            id='00000094-0000-0000-0000-000000000000',
            remaining_prepaid_credits=69.34,
            total_amount=178.32,
            amount_spent=37.7,
            start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
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

