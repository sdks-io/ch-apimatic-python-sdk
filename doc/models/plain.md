
# Plain

*This model accepts additional fields of type Any.*

## Structure

`Plain`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Optional | Database username. |
| `password` | `str` | Optional | Database password. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.plain import Plain

plain = Plain(
    username='postgres_user',
    password='your_secure_password',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

