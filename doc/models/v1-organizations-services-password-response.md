
# V1 Organizations Services Password Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesPasswordResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ServicePasswordPatchResponse`](../../doc/models/service-password-patch-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_password_patch_response import ServicePasswordPatchResponse
from openapispecforclickhousecloud.models.v_1_organizations_services_password_response import V1OrganizationsServicesPasswordResponse

v_1_organizations_services_password_response = V1OrganizationsServicesPasswordResponse(
    status=200,
    request_id='0000060c-0000-0000-0000-000000000000',
    result=ServicePasswordPatchResponse(
        password='password0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

