
# Scim Patch Op

*This model accepts additional fields of type Any.*

## Structure

`ScimPatchOp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | Must include "urn:ietf:params:scim:api:messages:2.0:PatchOp". |
| `operations` | [`List[ScimPatchOperation]`](../../doc/models/scim-patch-operation.md) | Required | List of PATCH operations to apply. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.op import Op
from openapispecforclickhousecloud.models.scim_patch_op import ScimPatchOp
from openapispecforclickhousecloud.models.scim_patch_operation import ScimPatchOperation

scim_patch_op = ScimPatchOp(
    schemas=[
        'schemas1',
        'schemas0',
        'schemas9'
    ],
    operations=[
        ScimPatchOperation(
            op=Op.REPLACE,
            path='path0',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

