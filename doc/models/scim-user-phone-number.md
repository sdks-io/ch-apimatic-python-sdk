
# Scim User Phone Number

*This model accepts additional fields of type Any.*

## Structure

`ScimUserPhoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | Phone number value. |
| `mtype` | `str` | Optional | Type of phone number (e.g., "work", "home", "mobile"). |
| `primary` | `bool` | Optional | A Boolean value indicating the preferred phone number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_phone_number import ScimUserPhoneNumber

scim_user_phone_number = ScimUserPhoneNumber(
    value='value2',
    mtype='type0',
    primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

