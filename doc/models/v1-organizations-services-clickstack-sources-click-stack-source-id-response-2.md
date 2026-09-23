
# V1 Organizations Services Clickstack Sources Click Stack Source Id Response 2

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_sources_click_stack_source_id_response_2 import V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2

v_1_organizations_services_clickstack_sources_click_stack_source_id_response_2 = V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2(
    status=200,
    request_id='00002378-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

