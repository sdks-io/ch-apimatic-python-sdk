
# V1 Organizations Members Response 3

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsMembersResponse3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.v_1_organizations_members_response_3 import V1OrganizationsMembersResponse3

v_1_organizations_members_response_3 = V1OrganizationsMembersResponse3(
    status=200,
    request_id='000023d0-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

