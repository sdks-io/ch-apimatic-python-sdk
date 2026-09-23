
# Byoc Config

*This model accepts additional fields of type Any.*

## Structure

`ByocConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique identifier of the BYOC configuration |
| `state` | [`State1`](../../doc/models/state-1.md) | Optional | State of the infrastructure |
| `account_name` | `str` | Optional | Name of the account |
| `region_id` | [`RegionId`](../../doc/models/region-id.md) | Optional | Region for which the BYOC has been configured and where it is possible to create services |
| `cloud_provider` | [`CloudProvider2`](../../doc/models/cloud-provider-2.md) | Optional | Cloud provider of the region |
| `display_name` | `str` | Optional | Human readable name for infrastructure |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.byoc_config import ByocConfig
from openapispecforclickhousecloud.models.cloud_provider_2 import CloudProvider2
from openapispecforclickhousecloud.models.region_id import RegionId
from openapispecforclickhousecloud.models.state_1 import State1

byoc_config = ByocConfig(
    id='id4',
    state=State1.INFRATERMINATED,
    account_name='accountName8',
    region_id=RegionId.EUWEST2,
    cloud_provider=CloudProvider2.GCP,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

