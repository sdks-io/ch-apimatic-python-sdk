
# Service Password Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ServicePasswordPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_password_hash` | `str` | Optional | Optional password hash. Used to avoid password transmission over network. If not provided a new password is generated and is provided in the response. Otherwise this hash is used. Algorithm: echo -n "yourpassword" \| sha256sum \| tr -d '-' \| xxd -r -p \| base64 |
| `new_double_sha_1_hash` | `str` | Optional | Optional double SHA1 password hash for MySQL protocol. If newPasswordHash is not provided this key will be ignored and the generated password will be used. Algorithm: echo -n "yourpassword" \| sha1sum \| tr -d '-' \| xxd -r -p \| sha1sum \| tr -d '-' |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_password_patch_request import ServicePasswordPatchRequest

service_password_patch_request = ServicePasswordPatchRequest(
    new_password_hash='newPasswordHash6',
    new_double_sha_1_hash='newDoubleSha1Hash6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

