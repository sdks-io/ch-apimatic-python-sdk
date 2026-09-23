
# Service Clickhouse Settings List

*This model accepts additional fields of type Any.*

## Structure

`ServiceClickhouseSettingsList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settings` | [`List[ServiceClickhouseSetting]`](../../doc/models/service-clickhouse-setting.md) | Optional | List of ClickHouse settings with their current values. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting import ServiceClickhouseSetting
from openapispecforclickhousecloud.models.service_clickhouse_settings_list import ServiceClickhouseSettingsList

service_clickhouse_settings_list = ServiceClickhouseSettingsList(
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
)
```

