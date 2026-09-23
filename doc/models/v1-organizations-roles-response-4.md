
# V1 Organizations Roles Response 4

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsRolesResponse4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.v_1_organizations_roles_response_4 import V1OrganizationsRolesResponse4

v_1_organizations_roles_response_4 = V1OrganizationsRolesResponse4(
    status=200,
    request_id='0000069c-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

