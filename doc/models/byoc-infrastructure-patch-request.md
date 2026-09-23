
# Byoc Infrastructure Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ByocInfrastructurePatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | Human readable name for infrastructure object |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.byoc_infrastructure_patch_request import ByocInfrastructurePatchRequest

byoc_infrastructure_patch_request = ByocInfrastructurePatchRequest(
    display_name='displayName4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

