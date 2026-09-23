
# Organization

*This model accepts additional fields of type Any.*

## Structure

`Organization`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique organization ID. |
| `created_at` | `datetime` | Optional | The timestamp the organization was created. ISO-8601. |
| `name` | `str` | Optional | Name of the organization. |
| `private_endpoints` | [`List[OrganizationPrivateEndpoint]`](../../doc/models/organization-private-endpoint.md) | Optional | List of private endpoints for organization |
| `byoc_config` | [`List[ByocConfig]`](../../doc/models/byoc-config.md) | Optional | BYOC configuration for the organization |
| `enable_core_dumps` | `bool` | Optional | Whether crash reports (core dumps) collection is enabled for services in the organization. When disabled at the organization level, individual services cannot enable crash reports. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.byoc_config import ByocConfig
from openapispecforclickhousecloud.models.cloud_provider_1 import CloudProvider1
from openapispecforclickhousecloud.models.cloud_provider_2 import CloudProvider2
from openapispecforclickhousecloud.models.organization import Organization
from openapispecforclickhousecloud.models.organization_private_endpoint import OrganizationPrivateEndpoint
from openapispecforclickhousecloud.models.region_1 import Region1
from openapispecforclickhousecloud.models.region_id import RegionId
from openapispecforclickhousecloud.models.state_1 import State1

organization = Organization(
    id='00001ed8-0000-0000-0000-000000000000',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    name='name6',
    private_endpoints=[
        OrganizationPrivateEndpoint(
            id='id0',
            description='description0',
            cloud_provider=CloudProvider1.AWS,
            region=Region1.USCENTRAL1,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    byoc_config=[
        ByocConfig(
            id='id0',
            state=State1.INFRAPROVISIONING,
            account_name='accountName4',
            region_id=RegionId.APSOUTHEAST2,
            cloud_provider=CloudProvider2.AZURE,
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

