
# Service Clickhouse Settings Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ServiceClickhouseSettingsPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settings` | Dict[str, str \| int] | Required | Setting value in its native JSON type. Use the settings schema endpoint for per-setting constraints. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_settings_patch_request import ServiceClickhouseSettingsPatchRequest

service_clickhouse_settings_patch_request = ServiceClickhouseSettingsPatchRequest(
    settings={
        'compatibility': '26.2',
        'max_query_size': 262144
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

