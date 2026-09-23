
# Scim Service Provider Config Filter

*This model accepts additional fields of type Any.*

## Structure

`ScimServiceProviderConfigFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `supported` | `bool` | Required | Whether filter is supported. |
| `max_results` | `int` | Required | Maximum number of results per filter query. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_service_provider_config_filter import ScimServiceProviderConfigFilter

scim_service_provider_config_filter = ScimServiceProviderConfigFilter(
    supported=False,
    max_results=238,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

