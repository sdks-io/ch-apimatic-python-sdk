
# Snapshot Configuration

*This model accepts additional fields of type Any.*

## Structure

`SnapshotConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Whether scheduled snapshots are enabled for the service. |
| `gap` | `float` | Optional | Interval between snapshots, in minutes. Set together with timeFrame; only supported preset pairs are accepted. |
| `time_frame` | `float` | Optional | Retention window the snapshots cover, in minutes. Set together with gap; only supported preset pairs are accepted. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.snapshot_configuration import SnapshotConfiguration

snapshot_configuration = SnapshotConfiguration(
    enabled=False,
    gap=34.02,
    time_frame=155.84,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

