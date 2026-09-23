
# V1 Organizations Services Clickpipes Cdc Scaling Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesCdcScalingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickPipesCdcScaling`](../../doc/models/click-pipes-cdc-scaling.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipes_cdc_scaling import ClickPipesCdcScaling
from openapispecforclickhousecloud.models.v_1_organizations_services_clickpipes_cdc_scaling_response import V1OrganizationsServicesClickpipesCdcScalingResponse

v_1_organizations_services_clickpipes_cdc_scaling_response = V1OrganizationsServicesClickpipesCdcScalingResponse(
    status=200,
    request_id='00001156-0000-0000-0000-000000000000',
    result=ClickPipesCdcScaling(
        replica_cpu_millicores=1000,
        replica_memory_gb=128,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

