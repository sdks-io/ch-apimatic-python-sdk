
# Service Clickhouse Setting Schema Entry

*This model accepts additional fields of type Any.*

## Structure

`ServiceClickhouseSettingSchemaEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the setting. |
| `mtype` | `str` | Optional | Data type of the setting value. |
| `description` | `str` | Optional | Description of the setting. |
| `enum` | `List[int]` | Optional | List of allowed values, if the setting is an enum. |
| `warning` | `str` | Optional | Warning message about potential disruptive effects of changing this setting. |
| `deprecation_notice` | `str` | Optional | Deprecation notice, if applicable. |
| `example` | `str` | Optional | Example value for the setting. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting_schema_entry import ServiceClickhouseSettingSchemaEntry

service_clickhouse_setting_schema_entry = ServiceClickhouseSettingSchemaEntry(
    name='compatibility',
    mtype='string',
    description='ClickHouse version compatibility setting.',
    enum=[
        0,
        1
    ],
    warning='Changing this setting without comprehensive testing can cause instability.',
    deprecation_notice='This setting may become obsolete with Cloud v2 stateless workers.',
    example='24.8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

