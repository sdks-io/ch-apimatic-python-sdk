
# Organization Patch Private Endpoint

*This model accepts additional fields of type Any.*

## Structure

`OrganizationPatchPrivateEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Private endpoint identifier |
| `description` | `str` | Optional | Optional description of private endpoint |
| `cloud_provider` | [`CloudProvider1`](../../doc/models/cloud-provider-1.md) | Optional | Cloud provider in which the private endpoint is lcoated |
| `region` | [`Region1`](../../doc/models/region-1.md) | Optional | Region in which the private endpoint is located |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider_1 import CloudProvider1
from openapispecforclickhousecloud.models.organization_patch_private_endpoint import OrganizationPatchPrivateEndpoint
from openapispecforclickhousecloud.models.region_1 import Region1

organization_patch_private_endpoint = OrganizationPatchPrivateEndpoint(
    id='id4',
    description='description6',
    cloud_provider=CloudProvider1.AWS,
    region=Region1.APSOUTH1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

