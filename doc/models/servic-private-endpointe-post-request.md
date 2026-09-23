
# Servic Private Endpointe Post Request

*This model accepts additional fields of type Any.*

## Structure

`ServicPrivateEndpointePostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Private endpoint identifier |
| `description` | `str` | Optional | Description of private endpoint |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.servic_private_endpointe_post_request import ServicPrivateEndpointePostRequest

servic_private_endpointe_post_request = ServicPrivateEndpointePostRequest(
    id='id2',
    description='description2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

