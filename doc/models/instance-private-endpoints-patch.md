
# Instance Private Endpoints Patch

*This model accepts additional fields of type Any.*

## Structure

`InstancePrivateEndpointsPatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `add` | `List[str]` | Optional | Elements to add. Executed after "remove" part is processed. |
| `remove` | `List[str]` | Optional | Elements to remove. Executed before "add" part is processed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.instance_private_endpoints_patch import InstancePrivateEndpointsPatch

instance_private_endpoints_patch = InstancePrivateEndpointsPatch(
    add=[
        'add6'
    ],
    remove=[
        'remove9',
        'remove0',
        'remove1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

