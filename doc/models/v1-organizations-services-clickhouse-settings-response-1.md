
# V1 Organizations Services Clickhouse Settings Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickhouseSettingsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ServiceClickhouseSettingsPatchResponse`](../../doc/models/service-clickhouse-settings-patch-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting_warning import ServiceClickhouseSettingWarning
from openapispecforclickhousecloud.models.service_clickhouse_settings_patch_response import ServiceClickhouseSettingsPatchResponse
from openapispecforclickhousecloud.models.v_1_organizations_services_clickhouse_settings_response_1 import V1OrganizationsServicesClickhouseSettingsResponse1

v_1_organizations_services_clickhouse_settings_response_1 = V1OrganizationsServicesClickhouseSettingsResponse1(
    status=200,
    request_id='00001052-0000-0000-0000-000000000000',
    result=ServiceClickhouseSettingsPatchResponse(
        settings={
            'key0': 'String9',
            'key1': 'String0'
        },
        warnings=[
            ServiceClickhouseSettingWarning(
                name='name4',
                message='message4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ServiceClickhouseSettingWarning(
                name='name4',
                message='message4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ServiceClickhouseSettingWarning(
                name='name4',
                message='message4',
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

