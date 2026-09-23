
# Udf Argument

*This model accepts additional fields of type Any.*

## Structure

`UdfArgument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name of the argument. Required for Native and JSONEachRow formats.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `mtype` | `str` | Required | ClickHouse data type of the argument. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.udf_argument import UdfArgument

udf_argument = UdfArgument(
    name='name2',
    mtype='type8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

