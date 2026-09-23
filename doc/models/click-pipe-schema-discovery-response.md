
# Click Pipe Schema Discovery Response

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeSchemaDiscoveryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fields` | [`List[ClickPipeSchemaDiscoveryField]`](../../doc/models/click-pipe-schema-discovery-field.md) | Optional | Inferred schema fields with their ClickHouse data types. |
| `meta` | `Dict[str, str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_schema_discovery_field import ClickPipeSchemaDiscoveryField
from openapispecforclickhousecloud.models.click_pipe_schema_discovery_response import ClickPipeSchemaDiscoveryResponse

click_pipe_schema_discovery_response = ClickPipeSchemaDiscoveryResponse(
    fields=[
        ClickPipeSchemaDiscoveryField(
            name='name8',
            mtype='type2',
            optional=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickPipeSchemaDiscoveryField(
            name='name8',
            mtype='type2',
            optional=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
        'key0': 'meta5'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

