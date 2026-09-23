
# Service Clickhouse Settings Patch Response

*This model accepts additional fields of type Any.*

## Structure

`ServiceClickhouseSettingsPatchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settings` | Dict[str, str \| int] \| None | Optional | Setting value in its native JSON type. Use the settings schema endpoint for per-setting constraints. |
| `warnings` | [`List[ServiceClickhouseSettingWarning]`](../../doc/models/service-clickhouse-setting-warning.md) | Optional | Warnings for settings that may have disruptive effects. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting_warning import ServiceClickhouseSettingWarning
from openapispecforclickhousecloud.models.service_clickhouse_settings_patch_response import ServiceClickhouseSettingsPatchResponse

service_clickhouse_settings_patch_response = ServiceClickhouseSettingsPatchResponse(
    settings={
        'compatibility': '26.2',
        'max_query_size': 262144
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
)
```

