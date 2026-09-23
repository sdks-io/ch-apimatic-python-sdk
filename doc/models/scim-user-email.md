
# Scim User Email

*This model accepts additional fields of type Any.*

## Structure

`ScimUserEmail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Required | Email address value. |
| `mtype` | `str` | Optional | Type of email (e.g., "work", "home"). |
| `primary` | `bool` | Optional | A Boolean value indicating the primary email address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_email import ScimUserEmail

scim_user_email = ScimUserEmail(
    value='value2',
    mtype='type0',
    primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

