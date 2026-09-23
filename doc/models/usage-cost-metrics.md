
# Usage Cost Metrics

*This model accepts additional fields of type Any.*

## Structure

`UsageCostMetrics`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `storage_chc` | `float` | Optional | Cost of storage in ClickHouse Credits (CHCs). Applies to dataWarehouse entities. |
| `backup_chc` | `float` | Optional | Cost of backup in ClickHouse Credits (CHCs). Applies to dataWarehouse entities. |
| `compute_chc` | `float` | Optional | Cost of compute in ClickHouse Credits (CHCs). Applies to service and clickpipe entities. |
| `data_transfer_chc` | `float` | Optional | Cost of data transfer in ClickHouse Credits (CHCs). Applies to clickpipe entities. |
| `initial_load_chc` | `float` | Optional | Cost of initial load and resyncs in ClickHouse Credits (CHCs). Applies to clickpipe entities. |
| `public_data_transfer_chc` | `float` | Optional | Cost of data transfer in ClickHouse Credits (CHCs). Applies to service entities. |
| `inter_region_tier_1_data_transfer_chc` | `float` | Optional | Cost of tier1 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities. |
| `inter_region_tier_2_data_transfer_chc` | `float` | Optional | Cost of tier2 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities. |
| `inter_region_tier_3_data_transfer_chc` | `float` | Optional | Cost of tier3 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities. |
| `inter_region_tier_4_data_transfer_chc` | `float` | Optional | Cost of tier4 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.usage_cost_metrics import UsageCostMetrics

usage_cost_metrics = UsageCostMetrics(
    storage_chc=68.38,
    backup_chc=101.66,
    compute_chc=87.1,
    data_transfer_chc=188.62,
    initial_load_chc=110.34,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

