
# Organization Patch Request

*This model accepts additional fields of type Any.*

## Structure

`OrganizationPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the organization. |
| `private_endpoints` | [`OrganizationPrivateEndpointsPatch`](../../doc/models/organization-private-endpoints-patch.md) | Optional | - |
| `enable_core_dumps` | `bool` | Optional | Whether crash reports (core dumps) collection is enabled for services in the organization. When disabled at the organization level, individual services cannot enable crash reports. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider_1 import CloudProvider1
from openapispecforclickhousecloud.models.organization_patch_private_endpoint import OrganizationPatchPrivateEndpoint
from openapispecforclickhousecloud.models.organization_patch_request import OrganizationPatchRequest
from openapispecforclickhousecloud.models.organization_private_endpoints_patch import OrganizationPrivateEndpointsPatch
from openapispecforclickhousecloud.models.region_1 import Region1

organization_patch_request = OrganizationPatchRequest(
    name='name2',
    private_endpoints=OrganizationPrivateEndpointsPatch(
        add=[
            OrganizationPatchPrivateEndpoint(
                id='id6',
                description='description4',
                cloud_provider=CloudProvider1.AZURE,
                region=Region1.APSOUTHEAST2,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            OrganizationPatchPrivateEndpoint(
                id='id6',
                description='description4',
                cloud_provider=CloudProvider1.AZURE,
                region=Region1.APSOUTHEAST2,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            OrganizationPatchPrivateEndpoint(
                id='id6',
                description='description4',
                cloud_provider=CloudProvider1.AZURE,
                region=Region1.APSOUTHEAST2,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        remove=[
            OrganizationPatchPrivateEndpoint(
                id='id0',
                description='description0',
                cloud_provider=CloudProvider1.AZURE,
                region=Region1.APSOUTH1,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    enable_core_dumps=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

