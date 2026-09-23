
# Click Pipe Scaling

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeScaling`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `replicas` | `int` | Optional | Desired number of replicas. Only for scalable pipes.<br><br>**Constraints**: `>= 1`, `<= 40` |
| `concurrency` | `int` | Optional | Desired number of concurrency. Only for S3 pipes. If set to 0, concurrency is auto-scaled based on the cluster memory. |
| `replica_cpu_millicores` | `int` | Optional | CPU in millicores for each replica. Only for streaming pipes.<br><br>**Constraints**: `>= 125`, `<= 2000` |
| `replica_memory_gb` | `float` | Optional | Memory in GB for each replica. Only for streaming pipes.<br><br>**Constraints**: `>= 0.5`, `<= 8` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_scaling import ClickPipeScaling

click_pipe_scaling = ClickPipeScaling(
    replicas=40,
    concurrency=102,
    replica_cpu_millicores=125,
    replica_memory_gb=8,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

