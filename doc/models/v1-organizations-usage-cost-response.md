
# V1 Organizations Usage Cost Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsUsageCostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`UsageCost`](../../doc/models/usage-cost.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.entity_type import EntityType
from openapispecforclickhousecloud.models.usage_cost import UsageCost
from openapispecforclickhousecloud.models.usage_cost_record import UsageCostRecord
from openapispecforclickhousecloud.models.v_1_organizations_usage_cost_response import V1OrganizationsUsageCostResponse

v_1_organizations_usage_cost_response = V1OrganizationsUsageCostResponse(
    status=200,
    request_id='000012fe-0000-0000-0000-000000000000',
    result=UsageCost(
        grand_total_chc=51.94,
        costs=[
            UsageCostRecord(
                data_warehouse_id='00001eea-0000-0000-0000-000000000000',
                service_id='000004d4-0000-0000-0000-000000000000',
                date=dateutil.parser.parse('2016-03-13').date(),
                entity_type=EntityType.CLICKPIPE,
                entity_id='000006d6-0000-0000-0000-000000000000',
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

