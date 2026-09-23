
# V1 Organizations Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[Organization]`](../../doc/models/organization.md) | Optional | - |
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
from openapispecforclickhousecloud.models.v_1_organizations_response import V1OrganizationsResponse

v_1_organizations_response = V1OrganizationsResponse(
    status=200,
    request_id='00000b24-0000-0000-0000-000000000000',
    result=[
        Organization(
            id='000002b8-0000-0000-0000-000000000000',
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
                ),
                OrganizationPrivateEndpoint(
                    id='id0',
                    description='description0',
                    cloud_provider=CloudProvider1.AWS,
                    region=Region1.USCENTRAL1,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
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
                ),
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
        ),
        Organization(
            id='000002b8-0000-0000-0000-000000000000',
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
                ),
                OrganizationPrivateEndpoint(
                    id='id0',
                    description='description0',
                    cloud_provider=CloudProvider1.AWS,
                    region=Region1.USCENTRAL1,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
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
                ),
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
        ),
        Organization(
            id='000002b8-0000-0000-0000-000000000000',
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
                ),
                OrganizationPrivateEndpoint(
                    id='id0',
                    description='description0',
                    cloud_provider=CloudProvider1.AWS,
                    region=Region1.USCENTRAL1,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
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
                ),
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

