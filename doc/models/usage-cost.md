
# Usage Cost

*This model accepts additional fields of type Any.*

## Structure

`UsageCost`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grand_total_chc` | `float` | Optional | Grand total cost of usage in ClickHouse Credits (CHCs). |
| `costs` | [`List[UsageCostRecord]`](../../doc/models/usage-cost-record.md) | Optional | List of daily, per-entity usage cost records. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.entity_type import EntityType
from openapispecforclickhousecloud.models.usage_cost import UsageCost
from openapispecforclickhousecloud.models.usage_cost_record import UsageCostRecord

usage_cost = UsageCost(
    grand_total_chc=84.82,
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
        ),
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
)
```

