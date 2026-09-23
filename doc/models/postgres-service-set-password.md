
# Postgres Service Set Password

*This model accepts additional fields of type Any.*

## Structure

`PostgresServiceSetPassword`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `password` | `str` | Optional | Optional password. If not provided a new password is generated and provided in the response. Must contain:<br><br>* At least one lowercase letter<br>* At least one uppercase letter<br>* At least one digit<br><br>**Constraints**: *Pattern*: `[a-z]` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_service_set_password import PostgresServiceSetPassword

postgres_service_set_password = PostgresServiceSetPassword(
    password='password6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

