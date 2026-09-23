
# Service Clickhouse Settings Schema

*This model accepts additional fields of type Any.*

## Structure

`ServiceClickhouseSettingsSchema`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settings` | [`List[ServiceClickhouseSettingSchemaEntry]`](../../doc/models/service-clickhouse-setting-schema-entry.md) | Optional | List of all configurable ClickHouse settings with their types, descriptions, and constraints. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting_schema_entry import ServiceClickhouseSettingSchemaEntry
from openapispecforclickhousecloud.models.service_clickhouse_settings_schema import ServiceClickhouseSettingsSchema

service_clickhouse_settings_schema = ServiceClickhouseSettingsSchema(
    settings=[
        ServiceClickhouseSettingSchemaEntry(
            name='name8',
            mtype='type2',
            description='description8',
            enum=[
                234
            ],
            warning='warning6',
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

