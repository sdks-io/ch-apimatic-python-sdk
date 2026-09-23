
# Instance Tags Patch

*This model accepts additional fields of type Any.*

## Structure

`InstanceTagsPatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `add` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Elements to add. Executed after "remove" part is processed.<br><br>**Constraints**: *Maximum Items*: `50` |
| `remove` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Elements to remove. Executed before "add" part is processed.<br><br>**Constraints**: *Maximum Items*: `50` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.instance_tags_patch import InstanceTagsPatch
from openapispecforclickhousecloud.models.resource_tags_v_1 import ResourceTagsV1

instance_tags_patch = InstanceTagsPatch(
    add=[
        ResourceTagsV1(
            key='key6',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ResourceTagsV1(
            key='key6',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ResourceTagsV1(
            key='key6',
            value='value8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    remove=[
        ResourceTagsV1(
            key='key0',
            value='value2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ResourceTagsV1(
            key='key0',
            value='value2',
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

