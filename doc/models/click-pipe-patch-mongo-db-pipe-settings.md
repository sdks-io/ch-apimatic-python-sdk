
# Click Pipe Patch Mongo Db Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchMongoDbPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sync_interval_seconds` | `int` | Optional | Interval in seconds to sync data from MongoDB during CDC replication.<br><br>**Constraints**: `>= 1` |
| `pull_batch_size` | `int` | Optional | Number of rows to pull in each batch during CDC replication.<br><br>**Constraints**: `>= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_patch_mongo_db_pipe_settings import ClickPipePatchMongoDbPipeSettings

click_pipe_patch_mongo_db_pipe_settings = ClickPipePatchMongoDbPipeSettings(
    sync_interval_seconds=60,
    pull_batch_size=100000,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

