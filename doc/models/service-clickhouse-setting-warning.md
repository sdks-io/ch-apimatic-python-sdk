
# Service Clickhouse Setting Warning

*This model accepts additional fields of type Any.*

## Structure

`ServiceClickhouseSettingWarning`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the setting the warning applies to. |
| `message` | `str` | Optional | Warning message. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting_warning import ServiceClickhouseSettingWarning

service_clickhouse_setting_warning = ServiceClickhouseSettingWarning(
    name='compatibility',
    message='Changing the compatibility version without comprehensive testing can cause query failures or instability.',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

