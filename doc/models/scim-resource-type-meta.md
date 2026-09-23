
# Scim Resource Type Meta

*This model accepts additional fields of type Any.*

## Structure

`ScimResourceTypeMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resource_type` | `str` | Required | The resource type. |
| `location` | `str` | Required | The URI of this resource. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_resource_type_meta import ScimResourceTypeMeta

scim_resource_type_meta = ScimResourceTypeMeta(
    resource_type='resourceType6',
    location='location6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

