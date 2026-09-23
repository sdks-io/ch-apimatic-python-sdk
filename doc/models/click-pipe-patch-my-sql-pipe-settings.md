
# Click Pipe Patch My Sql Pipe Settings

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchMySqlPipeSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sync_interval_seconds` | `int` | Optional | Interval in seconds to sync data from MySQL during CDC replication.<br><br>**Constraints**: `>= 1` |
| `pull_batch_size` | `int` | Optional | Number of rows to pull in each batch during CDC replication.<br><br>**Constraints**: `>= 1` |
| `use_compression` | `bool` | Optional | Enable compression for the MySQL connection. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_patch_my_sql_pipe_settings import ClickPipePatchMySqlPipeSettings

click_pipe_patch_my_sql_pipe_settings = ClickPipePatchMySqlPipeSettings(
    sync_interval_seconds=60,
    pull_batch_size=1000,
    use_compression=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

