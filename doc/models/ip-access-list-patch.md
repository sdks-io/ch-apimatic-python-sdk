
# Ip Access List Patch

*This model accepts additional fields of type Any.*

## Structure

`IpAccessListPatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `add` | [`List[IpAccessListEntry]`](../../doc/models/ip-access-list-entry.md) | Optional | Elements to add. Executed after "remove" part is processed. |
| `remove` | [`List[IpAccessListEntry]`](../../doc/models/ip-access-list-entry.md) | Optional | Elements to remove. Executed before "add" part is processed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.ip_access_list_entry import IpAccessListEntry
from openapispecforclickhousecloud.models.ip_access_list_patch import IpAccessListPatch

ip_access_list_patch = IpAccessListPatch(
    add=[
        IpAccessListEntry(
            source='source8',
            description='description4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IpAccessListEntry(
            source='source8',
            description='description4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IpAccessListEntry(
            source='source8',
            description='description4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    remove=[
        IpAccessListEntry(
            source='source6',
            description='description0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IpAccessListEntry(
            source='source6',
            description='description0',
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

