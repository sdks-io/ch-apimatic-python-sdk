
# Byoc Infrastructure Post Request

*This model accepts additional fields of type Any.*

## Structure

`ByocInfrastructurePostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region_id` | [`RegionId1`](../../doc/models/region-id-1.md) | Optional | Region in which the BYOC infrastructure will be located |
| `account_id` | `str` | Optional | Cloud account ID the BYOC infrastructure is configured for |
| `availability_zone_suffixes` | [`List[AvailabilityZoneSuffix]`](../../doc/models/availability-zone-suffix.md) | Optional | List of availability zone suffixes |
| `vpc_cidr_range` | `str` | Optional | CIDR range for VPC |
| `display_name` | `str` | Optional | Human readable name for infrastructure |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.availability_zone_suffix import AvailabilityZoneSuffix
from openapispecforclickhousecloud.models.byoc_infrastructure_post_request import ByocInfrastructurePostRequest
from openapispecforclickhousecloud.models.region_id_1 import RegionId1

byoc_infrastructure_post_request = ByocInfrastructurePostRequest(
    region_id=RegionId1.EUROPEWEST4,
    account_id='accountId8',
    availability_zone_suffixes=[
        AvailabilityZoneSuffix.A,
        AvailabilityZoneSuffix.B,
        AvailabilityZoneSuffix.C
    ],
    vpc_cidr_range='vpcCidrRange8',
    display_name='displayName4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

