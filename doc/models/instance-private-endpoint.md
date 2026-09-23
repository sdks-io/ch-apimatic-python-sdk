
# Instance Private Endpoint

*This model accepts additional fields of type Any.*

## Structure

`InstancePrivateEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Private endpoint identifier |
| `description` | `str` | Optional | Description of private endpoint |
| `cloud_provider` | [`CloudProvider1`](../../doc/models/cloud-provider-1.md) | Optional | Cloud provider in which the private endpoint is lcoated |
| `region` | [`Region1`](../../doc/models/region-1.md) | Optional | Region in which the private endpoint is located |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider_1 import CloudProvider1
from openapispecforclickhousecloud.models.instance_private_endpoint import InstancePrivateEndpoint
from openapispecforclickhousecloud.models.region_1 import Region1

instance_private_endpoint = InstancePrivateEndpoint(
    id='id2',
    description='description2',
    cloud_provider=CloudProvider1.AWS,
    region=Region1.USCENTRAL1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

