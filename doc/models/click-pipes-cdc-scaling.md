
# Click Pipes Cdc Scaling

*This model accepts additional fields of type Any.*

## Structure

`ClickPipesCdcScaling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `replica_cpu_millicores` | `int` | Optional | CPU in millicores for DB ClickPipes.<br><br>**Constraints**: `>= 1000`, `<= 32000`, *Multiple Of*: `1000` |
| `replica_memory_gb` | `float` | Optional | Memory in GiB for DB ClickPipes. Must be 4× the CPU core count.<br><br>**Constraints**: `>= 4`, `<= 128`, *Multiple Of*: `4` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipes_cdc_scaling import ClickPipesCdcScaling

click_pipes_cdc_scaling = ClickPipesCdcScaling(
    replica_cpu_millicores=2000,
    replica_memory_gb=8,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

