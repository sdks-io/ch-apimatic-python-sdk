
# Active Balance

*This model accepts additional fields of type Any.*

## Structure

`ActiveBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique ID of the prepaid balance. |
| `remaining_prepaid_credits` | `float` | Optional | Remaining credits available on this balance, in ClickHouse Credits (CHCs). |
| `total_amount` | `float` | Optional | Total credits granted on this balance, in ClickHouse Credits (CHCs). |
| `amount_spent` | `float` | Optional | Credits spent from this balance, in ClickHouse Credits (CHCs). |
| `start_date` | `datetime` | Optional | Date the balance became active. ISO-8601, based on the UTC timezone. |
| `expiration_date` | `datetime` | Optional | Date the balance expires. ISO-8601, based on the UTC timezone. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.active_balance import ActiveBalance

active_balance = ActiveBalance(
    id='00000ac0-0000-0000-0000-000000000000',
    remaining_prepaid_credits=195.38,
    total_amount=48.36,
    amount_spent=163.74,
    start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

