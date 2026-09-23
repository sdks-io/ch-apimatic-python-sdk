
# Resource Tags V1

*This model accepts additional fields of type Any.*

## Structure

`ResourceTagsV1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | Tag key. Must be alphanumeric with dashes, underscores and dots.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `128`, *Pattern*: `^[a-zA-Z0-9._-]+$` |
| `value` | `str` | Optional | Tag value. Must be alphanumeric with dashes, underscores and dots.<br><br>**Constraints**: *Maximum Length*: `256`, *Pattern*: `^[a-zA-Z0-9._-]+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
from openapispecforclickhousecloud.models.resource_tags_v_1 import ResourceTagsV1

resource_tags_v_1 = ResourceTagsV1(
    key='Environment',
    value='staging'
)
```

