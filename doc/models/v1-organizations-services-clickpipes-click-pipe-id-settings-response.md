
# V1 Organizations Services Clickpipes Click Pipe Id Settings Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickPipeSettings`](../../doc/models/click-pipe-settings.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_settings import ClickPipeSettings
from openapispecforclickhousecloud.models.v_1_organizations_services_clickpipes_click_pipe_id_settings_response import V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse

v_1_organizations_services_clickpipes_click_pipe_id_settings_response = V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse(
    status=200,
    request_id='00000ec8-0000-0000-0000-000000000000',
    result=ClickPipeSettings(
        streaming_max_insert_wait_ms=500,
        object_storage_concurrency=35,
        object_storage_polling_interval_ms=100,
        object_storage_max_insert_bytes=524288000,
        object_storage_max_file_count=90,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

