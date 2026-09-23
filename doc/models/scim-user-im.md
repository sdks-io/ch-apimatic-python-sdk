
# Scim User Im

*This model accepts additional fields of type Any.*

## Structure

`ScimUserIm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | Instant messaging address. |
| `mtype` | `str` | Optional | Type of IM address (e.g., "aim", "gtalk", "icq", "xmpp", "msn", "skype", "qq"). |
| `primary` | `bool` | Optional | A Boolean value indicating the preferred IM address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_im import ScimUserIm

scim_user_im = ScimUserIm(
    value='value8',
    mtype='type4',
    primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

