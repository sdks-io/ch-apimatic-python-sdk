
# Azure Event Hub

*This model accepts additional fields of type Any.*

## Structure

`AzureEventHub`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `connection_string` | `str` | Optional | Connection string for Azure EventHub source. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.azure_event_hub import AzureEventHub

azure_event_hub = AzureEventHub(
    connection_string='connectionString6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

