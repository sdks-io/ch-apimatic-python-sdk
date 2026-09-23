
# Scim Service Provider Config Patch

*This model accepts additional fields of type Any.*

## Structure

`ScimServiceProviderConfigPatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `supported` | `bool` | Required | Whether PATCH is supported. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_service_provider_config_patch import ScimServiceProviderConfigPatch

scim_service_provider_config_patch = ScimServiceProviderConfigPatch(
    supported=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

