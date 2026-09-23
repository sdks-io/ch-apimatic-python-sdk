
# Mutual Tls

*This model accepts additional fields of type Any.*

## Structure

`MutualTls`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `certificate` | `str` | Optional | PEM encoded client certificate for mTLS authentication. |
| `private_key` | `str` | Optional | PEM encoded client private key for mTLS authentication. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.mutual_tls import MutualTls

mutual_tls = MutualTls(
    certificate='certificate4',
    private_key='privateKey0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

