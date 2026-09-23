
# Scim Service Provider Config Meta

*This model accepts additional fields of type Any.*

## Structure

`ScimServiceProviderConfigMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resource_type` | `str` | Required | The resource type of this resource. |
| `location` | `str` | Required | The URI of this resource. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_service_provider_config_meta import ScimServiceProviderConfigMeta

scim_service_provider_config_meta = ScimServiceProviderConfigMeta(
    resource_type='resourceType6',
    location='location6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

