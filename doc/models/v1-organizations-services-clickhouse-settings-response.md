
# V1 Organizations Services Clickhouse Settings Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickhouseSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ServiceClickhouseSettingsList`](../../doc/models/service-clickhouse-settings-list.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting import ServiceClickhouseSetting
from openapispecforclickhousecloud.models.service_clickhouse_settings_list import ServiceClickhouseSettingsList
from openapispecforclickhousecloud.models.v_1_organizations_services_clickhouse_settings_response import V1OrganizationsServicesClickhouseSettingsResponse

v_1_organizations_services_clickhouse_settings_response = V1OrganizationsServicesClickhouseSettingsResponse(
    status=200,
    request_id='00001abe-0000-0000-0000-000000000000',
    result=ServiceClickhouseSettingsList(
        settings=[
            ServiceClickhouseSetting(
                name='name8',
                value='String1',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ServiceClickhouseSetting(
                name='name8',
                value='String1',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

