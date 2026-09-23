
# V1 Organizations Services Snapshot Configuration Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesSnapshotConfigurationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`SnapshotConfiguration`](../../doc/models/snapshot-configuration.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.snapshot_configuration import SnapshotConfiguration
from openapispecforclickhousecloud.models.v_1_organizations_services_snapshot_configuration_response import V1OrganizationsServicesSnapshotConfigurationResponse

v_1_organizations_services_snapshot_configuration_response = V1OrganizationsServicesSnapshotConfigurationResponse(
    status=200,
    request_id='00000ff8-0000-0000-0000-000000000000',
    result=SnapshotConfiguration(
        enabled=False,
        gap=65.7,
        time_frame=56.12,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

