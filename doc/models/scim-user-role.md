
# Scim User Role

*This model accepts additional fields of type Any.*

## Structure

`ScimUserRole`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | The value of a role; a string or label representing a collection of entitlements. No canonical types. |
| `display` | `str` | Optional | A human-readable name, primarily used for display purposes. |
| `mtype` | `str` | Optional | A label indicating the attribute's function. |
| `primary` | `bool` | Optional | A Boolean value indicating the primary or preferred role. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_role import ScimUserRole

scim_user_role = ScimUserRole(
    value='value6',
    display='display6',
    mtype='type6',
    primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

