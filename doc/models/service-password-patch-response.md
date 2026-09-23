
# Service Password Patch Response

*This model accepts additional fields of type Any.*

## Structure

`ServicePasswordPatchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `password` | `str` | Optional | New service password. Provided only if there was no 'newPasswordHash' in the request |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_password_patch_response import ServicePasswordPatchResponse

service_password_patch_response = ServicePasswordPatchResponse(
    password='password2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

