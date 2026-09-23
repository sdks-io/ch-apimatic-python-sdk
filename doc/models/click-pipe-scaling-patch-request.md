
# Click Pipe Scaling Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeScalingPatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `replicas` | `int` | Optional | Number of replicas to scale to. Use to scale Kafka pipes.<br><br>**Constraints**: `>= 1`, `<= 40` |
| `concurrency` | `int` | Optional | Number of concurrency to scale to. Use to scale S3 pipes.<br><br>**Constraints**: `>= 0`, `<= 34` |
| `replica_cpu_millicores` | `int` | Optional | CPU in millicores for each replica. Use to scale streaming pipes.<br><br>**Constraints**: `>= 125`, `<= 2000` |
| `replica_memory_gb` | `float` | Optional | Memory in GB for each replica. Use to scale streaming pipes.<br><br>**Constraints**: `>= 0.5`, `<= 8` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_scaling_patch_request import ClickPipeScalingPatchRequest

click_pipe_scaling_patch_request = ClickPipeScalingPatchRequest(
    replicas=40,
    concurrency=32,
    replica_cpu_millicores=202,
    replica_memory_gb=8,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

