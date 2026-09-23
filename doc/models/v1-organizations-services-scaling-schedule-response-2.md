
# V1 Organizations Services Scaling Schedule Response 2

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesScalingScheduleResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.v_1_organizations_services_scaling_schedule_response_2 import V1OrganizationsServicesScalingScheduleResponse2

v_1_organizations_services_scaling_schedule_response_2 = V1OrganizationsServicesScalingScheduleResponse2(
    status=200,
    request_id='0000176a-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

