
# Scim Group Member

*This model accepts additional fields of type Any.*

## Structure

`ScimGroupMember`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Required | The identifier of the member (user ID). |
| `display` | `str` | Optional | A human-readable name for the member. |
| `mtype` | `str` | Optional | Indicates the type of resource, typically "User". |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_group_member import ScimGroupMember

scim_group_member = ScimGroupMember(
    value='value6',
    display='display6',
    mtype='type6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

