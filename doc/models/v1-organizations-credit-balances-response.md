
# V1 Organizations Credit Balances Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsCreditBalancesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`CreditBalances`](../../doc/models/credit-balances.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.credit_balance import CreditBalance
from openapispecforclickhousecloud.models.credit_balances import CreditBalances
from openapispecforclickhousecloud.models.type_21 import Type21
from openapispecforclickhousecloud.models.v_1_organizations_credit_balances_response import V1OrganizationsCreditBalancesResponse

v_1_organizations_credit_balances_response = V1OrganizationsCreditBalancesResponse(
    status=200,
    request_id='000014ca-0000-0000-0000-000000000000',
    result=CreditBalances(
        total_remaining_credits=9.1,
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
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

