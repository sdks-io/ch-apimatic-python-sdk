
# Udf Argument Output

## Structure

`UdfArgumentOutput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name of the argument. Required for Native and JSONEachRow formats.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `mtype` | `str` | Required | ClickHouse data type of the argument. |

## Example

```python
from openapispecforclickhousecloud.models.udf_argument_output import UdfArgumentOutput

udf_argument_output = UdfArgumentOutput(
    name='name2',
    mtype='type2'
)
```

