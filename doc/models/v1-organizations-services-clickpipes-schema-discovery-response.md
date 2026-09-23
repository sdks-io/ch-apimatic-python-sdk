
# V1 Organizations Services Clickpipes Schema Discovery Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesSchemaDiscoveryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickPipeSchemaDiscoveryResponse`](../../doc/models/click-pipe-schema-discovery-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_schema_discovery_field import ClickPipeSchemaDiscoveryField
from openapispecforclickhousecloud.models.click_pipe_schema_discovery_response import ClickPipeSchemaDiscoveryResponse
from openapispecforclickhousecloud.models.v_1_organizations_services_clickpipes_schema_discovery_response import V1OrganizationsServicesClickpipesSchemaDiscoveryResponse

v_1_organizations_services_clickpipes_schema_discovery_response = V1OrganizationsServicesClickpipesSchemaDiscoveryResponse(
    status=200,
    request_id='00000a26-0000-0000-0000-000000000000',
    result=ClickPipeSchemaDiscoveryResponse(
        fields=[
            ClickPipeSchemaDiscoveryField(
                name='name8',
                mtype='type2',
                optional=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        meta={
            'key0': 'meta5',
            'key1': 'meta4',
            'key2': 'meta3'
        },
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

