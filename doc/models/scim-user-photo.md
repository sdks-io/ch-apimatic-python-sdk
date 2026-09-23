
# Scim User Photo

*This model accepts additional fields of type Any.*

## Structure

`ScimUserPhoto`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | URL of a photo of the User. |
| `mtype` | `str` | Optional | Type of photo (e.g., "photo", "thumbnail"). |
| `primary` | `bool` | Optional | A Boolean value indicating the preferred photo. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_photo import ScimUserPhoto

scim_user_photo = ScimUserPhoto(
    value='value2',
    mtype='type0',
    primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

