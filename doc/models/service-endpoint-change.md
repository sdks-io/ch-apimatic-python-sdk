
# Service Endpoint Change

*This model accepts additional fields of type Any.*

## Structure

`ServiceEndpointChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `protocol` | [`Protocol1`](../../doc/models/protocol-1.md) | Optional | Endpoint protocol |
| `enabled` | `bool` | Optional | Enable or disable the endpoint |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.protocol_1 import Protocol1
from openapispecforclickhousecloud.models.service_endpoint_change import ServiceEndpointChange

service_endpoint_change = ServiceEndpointChange(
    protocol=Protocol1.MYSQL,
    enabled=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

