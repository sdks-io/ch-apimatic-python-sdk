
# Scim Service Provider Config Bulk

*This model accepts additional fields of type Any.*

## Structure

`ScimServiceProviderConfigBulk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `supported` | `bool` | Required | Whether bulk operations are supported. |
| `max_operations` | `int` | Required | Maximum number of bulk operations per request. |
| `max_payload_size` | `int` | Required | Maximum payload size for bulk requests in bytes. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_service_provider_config_bulk import ScimServiceProviderConfigBulk

scim_service_provider_config_bulk = ScimServiceProviderConfigBulk(
    supported=False,
    max_operations=164,
    max_payload_size=208,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

