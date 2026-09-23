
# V1 Organizations Byoc Infrastructure Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsByocInfrastructureResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ByocConfig`](../../doc/models/byoc-config.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.byoc_config import ByocConfig
from openapispecforclickhousecloud.models.cloud_provider_2 import CloudProvider2
from openapispecforclickhousecloud.models.region_id import RegionId
from openapispecforclickhousecloud.models.state_1 import State1
from openapispecforclickhousecloud.models.v_1_organizations_byoc_infrastructure_response import V1OrganizationsByocInfrastructureResponse

v_1_organizations_byoc_infrastructure_response = V1OrganizationsByocInfrastructureResponse(
    status=200,
    request_id='000000d6-0000-0000-0000-000000000000',
    result=ByocConfig(
        id='id6',
        state=State1.INFRAREADY,
        account_name='accountName0',
        region_id=RegionId.USWEST2,
        cloud_provider=CloudProvider2.AZURE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

