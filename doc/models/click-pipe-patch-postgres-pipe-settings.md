
# Click Pipe Patch Postgres Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchPostgresPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sync_interval_seconds` | `int` | Optional | Interval in seconds to sync data from Postgres during CDC replication.<br><br>**Constraints**: `>= 1` |
| `pull_batch_size` | `int` | Optional | Number of rows to pull in each batch during CDC replication.<br><br>**Constraints**: `>= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_patch_postgres_pipe_settings import ClickPipePatchPostgresPipeSettings

click_pipe_patch_postgres_pipe_settings = ClickPipePatchPostgresPipeSettings(
    sync_interval_seconds=60,
    pull_batch_size=1000,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

