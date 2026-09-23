
# Organization Private Endpoints Patch

*This model accepts additional fields of type Any.*

## Structure

`OrganizationPrivateEndpointsPatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `add` | [`List[OrganizationPatchPrivateEndpoint]`](../../doc/models/organization-patch-private-endpoint.md) | Optional | DEPRECATED. Elements to add. Executed after "remove" part is processed. Please use the `Update Service Basic Details` endpoint with the `privateEndpointIds` field instead to modify the private endpoints. |
| `remove` | [`List[OrganizationPatchPrivateEndpoint]`](../../doc/models/organization-patch-private-endpoint.md) | Optional | Elements to remove. Executed before "add" part is processed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.cloud_provider_1 import CloudProvider1
from openapispecforclickhousecloud.models.organization_patch_private_endpoint import OrganizationPatchPrivateEndpoint
from openapispecforclickhousecloud.models.organization_private_endpoints_patch import OrganizationPrivateEndpointsPatch
from openapispecforclickhousecloud.models.region_1 import Region1

organization_private_endpoints_patch = OrganizationPrivateEndpointsPatch(
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
        ),
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
)
```

