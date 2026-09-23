
# Scim Authentication Scheme

*This model accepts additional fields of type Any.*

## Structure

`ScimAuthenticationScheme`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | The authentication scheme type (e.g., "httpbasic", "oauthbearertoken"). |
| `name` | `str` | Required | The common authentication scheme name. |
| `description` | `str` | Required | A description of the authentication scheme. |
| `spec_uri` | `str` | Optional | An HTTP-addressable URL pointing to the scheme specification. |
| `primary` | `bool` | Optional | A Boolean value indicating the primary authentication scheme. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_authentication_scheme import ScimAuthenticationScheme

scim_authentication_scheme = ScimAuthenticationScheme(
    mtype='type8',
    name='name2',
    description='description8',
    spec_uri='specUri6',
    primary=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

