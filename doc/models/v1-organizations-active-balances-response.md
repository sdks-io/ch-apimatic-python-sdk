
# V1 Organizations Active Balances Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsActiveBalancesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ActiveBalances`](../../doc/models/active-balances.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.active_balance import ActiveBalance
from openapispecforclickhousecloud.models.active_balances import ActiveBalances
from openapispecforclickhousecloud.models.v_1_organizations_active_balances_response import V1OrganizationsActiveBalancesResponse

v_1_organizations_active_balances_response = V1OrganizationsActiveBalancesResponse(
    status=200,
    request_id='0000096e-0000-0000-0000-000000000000',
    result=ActiveBalances(
        total_remaining_prepaid_credits=66.34,
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

