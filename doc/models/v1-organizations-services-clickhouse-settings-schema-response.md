
# V1 Organizations Services Clickhouse Settings Schema Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickhouseSettingsSchemaResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ServiceClickhouseSettingsSchema`](../../doc/models/service-clickhouse-settings-schema.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_clickhouse_setting_schema_entry import ServiceClickhouseSettingSchemaEntry
from openapispecforclickhousecloud.models.service_clickhouse_settings_schema import ServiceClickhouseSettingsSchema
from openapispecforclickhousecloud.models.v_1_organizations_services_clickhouse_settings_schema_response import V1OrganizationsServicesClickhouseSettingsSchemaResponse

v_1_organizations_services_clickhouse_settings_schema_response = V1OrganizationsServicesClickhouseSettingsSchemaResponse(
    status=200,
    request_id='00000028-0000-0000-0000-000000000000',
    result=ServiceClickhouseSettingsSchema(
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
            ),
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

