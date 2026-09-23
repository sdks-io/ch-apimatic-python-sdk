
# Postgres Service Password Resource

*This model accepts additional fields of type Any.*

## Structure

`PostgresServicePasswordResource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `password` | `str` | Optional | New Postgres superuser password. Provided only if there was no 'password' in the request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_service_password_resource import PostgresServicePasswordResource

postgres_service_password_resource = PostgresServicePasswordResource(
    password='password6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

