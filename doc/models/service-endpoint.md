
# Service Endpoint

*This model accepts additional fields of type Any.*

## Structure

`ServiceEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `protocol` | [`Protocol`](../../doc/models/protocol.md) | Optional | Endpoint protocol: 'https', 'nativesecure', 'mysql'. |
| `host` | `str` | Optional | Service host name |
| `port` | `float` | Optional | Numeric port |
| `username` | `str` | Optional | Optional username for the endpoint |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.protocol import Protocol
from openapispecforclickhousecloud.models.service_endpoint import ServiceEndpoint

service_endpoint = ServiceEndpoint(
    protocol=Protocol.MYSQL,
    host='host6',
    port=125.44,
    username='username4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

