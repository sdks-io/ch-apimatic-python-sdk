
# Usage Cost Record

*This model accepts additional fields of type Any.*

## Structure

`UsageCostRecord`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_warehouse_id` | `uuid\|str` | Optional | ID of the dataWarehouse this entity belongs to (or is). |
| `service_id` | `uuid\|str` | Optional | ID of the service this entity belongs to (or is). Set to null for dataWarehouse entities. |
| `date` | `date` | Optional | Date of the usage. ISO-8601 date, based on the UTC timezone. |
| `entity_type` | [`EntityType`](../../doc/models/entity-type.md) | Optional | Type of the entity. |
| `entity_id` | `uuid\|str` | Optional | Unique ID of the entity. |
| `entity_name` | `str` | Optional | Name of the entity. |
| `metrics` | [`UsageCostMetrics`](../../doc/models/usage-cost-metrics.md) | Optional | - |
| `total_chc` | `float` | Optional | Total cost of usage in ClickHouse Credits (CHCs) for this entity. |
| `locked` | `bool` | Optional | When true, the record is immutable. Unlocked records are subject to change until locked. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.entity_type import EntityType
from openapispecforclickhousecloud.models.usage_cost_record import UsageCostRecord

usage_cost_record = UsageCostRecord(
    data_warehouse_id='0000058a-0000-0000-0000-000000000000',
    service_id='00001284-0000-0000-0000-000000000000',
    date=dateutil.parser.parse('2016-03-13').date(),
    entity_type=EntityType.SERVICE,
    entity_id='00001486-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

