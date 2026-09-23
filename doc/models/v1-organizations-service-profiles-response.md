
# V1 Organizations Service Profiles Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServiceProfilesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[ServiceProfile]`](../../doc/models/service-profile.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_profile import ServiceProfile
from openapispecforclickhousecloud.models.v_1_organizations_service_profiles_response import V1OrganizationsServiceProfilesResponse

v_1_organizations_service_profiles_response = V1OrganizationsServiceProfilesResponse(
    status=200,
    request_id='000002e4-0000-0000-0000-000000000000',
    result=[
        ServiceProfile(
            profile='profile4',
            cpu_cores=88.02,
            memory_gi=246.54,
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

