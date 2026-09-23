
# Scim User Group

*This model accepts additional fields of type Any.*

## Structure

`ScimUserGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | The identifier of the group. |
| `display` | `str` | Optional | A human-readable name for the group. |
| `mtype` | `str` | Optional | A label indicating the attribute's function (e.g., "direct" or "indirect"). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_group import ScimUserGroup

scim_user_group = ScimUserGroup(
    value='value0',
    display='display0',
    mtype='type2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

