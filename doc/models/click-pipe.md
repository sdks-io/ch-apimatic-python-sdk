
# Click Pipe

*This model accepts additional fields of type Any.*

## Structure

`ClickPipe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique ClickPipe ID. |
| `service_id` | `uuid\|str` | Optional | ID of the service this ClickPipe belongs to. |
| `name` | `str` | Optional | Name of the ClickPipe.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `state` | [`State2`](../../doc/models/state-2.md) | Optional | Current lifecycle state of the ClickPipe. For database pipes: "Provisioning" (initial setup), "Setup" (configuring replication), "Snapshot" (initial data load), "Running" (actively replicating), "Pausing" (transitioning to paused state), "Paused" (temporarily paused), "Modifying" (applying configuration updates), "Resync" (swapping resync tables with original tables), "Failed" (error occurred), "Unknown". For streaming/object storage pipes (Kafka, Kinesis, S3): "Unknown" (initial state), "Provisioning" (setting up resources), "Running" (actively ingesting data), "Stopping" (transitioning to stopped state), "Stopped" (manually stopped, can be restarted), "Completed" (batch ingestion finished for object storage), "Failed" (error occurred, pipe stopped), "InternalError" (internal system error). |
| `scaling` | [`ClickPipeScaling`](../../doc/models/click-pipe-scaling.md) | Optional | - |
| `source` | [`ClickPipeSource`](../../doc/models/click-pipe-source.md) | Optional | - |
| `destination` | [`ClickPipeDestination`](../../doc/models/click-pipe-destination.md) | Optional | - |
| `field_mappings` | [`List[ClickPipeFieldMapping]`](../../doc/models/click-pipe-field-mapping.md) | Optional | Field mappings of the ClickPipe. Note that all destination columns must be included in the mappings. |
| `settings` | [`ClickPipeSettings`](../../doc/models/click-pipe-settings.md) | Optional | - |
| `created_at` | `datetime` | Optional | Creation timestamp of the ClickPipe in ISO 8601 format. |
| `updated_at` | `datetime` | Optional | Last update timestamp of the ClickPipe in ISO 8601 format. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe import ClickPipe
from openapispecforclickhousecloud.models.click_pipe_scaling import ClickPipeScaling
from openapispecforclickhousecloud.models.state_2 import State2

click_pipe = ClickPipe(
    id='000021d2-0000-0000-0000-000000000000',
    service_id='00000a02-0000-0000-0000-000000000000',
    name='my_postgres_pipe',
    state=State2.RUNNING,
    scaling=ClickPipeScaling(
        replicas=40,
        concurrency=26,
        replica_cpu_millicores=196,
        replica_memory_gb=8,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

