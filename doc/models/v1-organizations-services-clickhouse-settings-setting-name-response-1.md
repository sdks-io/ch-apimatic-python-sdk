
# V1 Organizations Services Clickhouse Settings Setting Name Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickhouseSettingsSettingNameResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.v_1_organizations_services_clickhouse_settings_setting_name_response_1 import V1OrganizationsServicesClickhouseSettingsSettingNameResponse1

v_1_organizations_services_clickhouse_settings_setting_name_response_1 = V1OrganizationsServicesClickhouseSettingsSettingNameResponse1(
    status=200,
    request_id='0000073a-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

