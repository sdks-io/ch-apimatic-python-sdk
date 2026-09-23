
# Scim X509 Certificate

*This model accepts additional fields of type Any.*

## Structure

`ScimX509Certificate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | The value of a X.509 certificate. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_x_509_certificate import ScimX509Certificate

scim_x_509_certificate = ScimX509Certificate(
    value='value6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

