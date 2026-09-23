
# Scim Patch Operation

*This model accepts additional fields of type Any.*

## Structure

`ScimPatchOperation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `op` | [`Op`](../../doc/models/op.md) | Required | The operation to perform. |
| `path` | `str` | Optional | Target attribute path (e.g. "active", "userName"). |
| `value` | `str` | Optional | New value for the attribute. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.op import Op
from openapispecforclickhousecloud.models.scim_patch_operation import ScimPatchOperation

scim_patch_operation = ScimPatchOperation(
    op=Op.REPLACE,
    path='path8',
    value='value6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

