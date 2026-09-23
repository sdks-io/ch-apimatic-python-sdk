
# V1 Organizations Services Clickhouse Settings Setting Name Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickhouseSettingsSettingNameResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ServiceClickhouseSetting`](../../doc/models/service-clickhouse-setting.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting import ServiceClickhouseSetting
from openapispecforclickhousecloud.models.v_1_organizations_services_clickhouse_settings_setting_name_response import V1OrganizationsServicesClickhouseSettingsSettingNameResponse

v_1_organizations_services_clickhouse_settings_setting_name_response = V1OrganizationsServicesClickhouseSettingsSettingNameResponse(
    status=200,
    request_id='00000a8a-0000-0000-0000-000000000000',
    result=ServiceClickhouseSetting(
        name='name6',
        value='String9',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

