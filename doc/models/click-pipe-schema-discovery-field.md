
# Click Pipe Schema Discovery Field

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeSchemaDiscoveryField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the inferred field. |
| `mtype` | `str` | Optional | Inferred ClickHouse data type of the field. |
| `optional` | `bool` | Optional | Whether the field is optional (nullable) in the source. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_schema_discovery_field import ClickPipeSchemaDiscoveryField

click_pipe_schema_discovery_field = ClickPipeSchemaDiscoveryField(
    name='user_id',
    mtype='Int64',
    optional=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

