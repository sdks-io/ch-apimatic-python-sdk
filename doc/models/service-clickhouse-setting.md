
# Service Clickhouse Setting

*This model accepts additional fields of type Any.*

## Structure

`ServiceClickhouseSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the setting. |
| `value` | str \| int \| None | Optional | Setting value in its native JSON type. Use the settings schema endpoint for per-setting constraints. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting import ServiceClickhouseSetting

service_clickhouse_setting = ServiceClickhouseSetting(
    name='compatibility',
    value='String9',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

