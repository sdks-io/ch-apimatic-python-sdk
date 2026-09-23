
# Scim User Entitlement

*This model accepts additional fields of type Any.*

## Structure

`ScimUserEntitlement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | The value of an entitlement. |
| `display` | `str` | Optional | A human-readable name for the entitlement. |
| `mtype` | `str` | Optional | A label indicating the attribute's function. |
| `primary` | `bool` | Optional | A Boolean value indicating the primary entitlement. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_entitlement import ScimUserEntitlement

scim_user_entitlement = ScimUserEntitlement(
    value='value6',
    display='display6',
    mtype='type4',
    primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

