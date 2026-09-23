
# V1 Organizations Services Clickpipes Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[ClickPipe]`](../../doc/models/click-pipe.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe import ClickPipe
from openapispecforclickhousecloud.models.click_pipe_scaling import ClickPipeScaling
from openapispecforclickhousecloud.models.state_2 import State2
from openapispecforclickhousecloud.models.v_1_organizations_services_clickpipes_response import V1OrganizationsServicesClickpipesResponse

v_1_organizations_services_clickpipes_response = V1OrganizationsServicesClickpipesResponse(
    status=200,
    request_id='00001d1e-0000-0000-0000-000000000000',
    result=[
        ClickPipe(
            id='000002b8-0000-0000-0000-000000000000',
            service_id='000011f8-0000-0000-0000-000000000000',
            name='name6',
            state=State2.PAUSING,
            scaling=ClickPipeScaling(
                replicas=40,
                concurrency=26,
                replica_cpu_millicores=196,
                replica_memory_gb=8,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickPipe(
            id='000002b8-0000-0000-0000-000000000000',
            service_id='000011f8-0000-0000-0000-000000000000',
            name='name6',
            state=State2.PAUSING,
            scaling=ClickPipeScaling(
                replicas=40,
                concurrency=26,
                replica_cpu_millicores=196,
                replica_memory_gb=8,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

