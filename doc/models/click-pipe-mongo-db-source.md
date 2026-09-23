
# Click Pipe Mongo Db Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeMongoDbSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uri` | `str` | Required | MongoDB connection URI. Supports both standard URIs (mongodb://...) and SRV URIs (mongodb+srv://...). Embedded credentials are redacted from API responses, so the returned value can differ from what was submitted. |
| `read_preference` | [`ReadPreference`](../../doc/models/read-preference.md) | Required | MongoDB read preference for replica set reads. |
| `tls_host` | `str` | Optional | TLS/SSL host for secure connections. |
| `disable_tls` | `bool` | Optional | Disable TLS for the MongoDB connection. Defaults to false (TLS enabled). |
| `skip_cert_verification` | `bool` | Optional | Skip TLS certificate verification for the MongoDB connection. Use with caution in production environments. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificate to validate the MongoDB server certificate. |
| `settings` | [`ClickPipeMongoDbPipeSettings`](../../doc/models/click-pipe-mongo-db-pipe-settings.md) | Optional | - |
| `table_mappings` | [`List[ClickPipeMongoDbPipeTableMapping]`](../../doc/models/click-pipe-mongo-db-pipe-table-mapping.md) | Optional | List of collection mappings defining which MongoDB collections to replicate and how they map to ClickHouse tables. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_mongo_db_pipe_settings import ClickPipeMongoDbPipeSettings
from openapispecforclickhousecloud.models.click_pipe_mongo_db_source import ClickPipeMongoDbSource
from openapispecforclickhousecloud.models.read_preference import ReadPreference
from openapispecforclickhousecloud.models.replication_mode import ReplicationMode

click_pipe_mongo_db_source = ClickPipeMongoDbSource(
    uri='mongodb+srv://cluster0.example.mongodb.net/mydb',
    read_preference=ReadPreference.SECONDARYPREFERRED,
    tls_host='cluster0.example.mongodb.net',
    disable_tls=False,
    skip_cert_verification=False,
    ca_certificate='-----BEGIN CERTIFICATE-----\n...',
    settings=ClickPipeMongoDbPipeSettings(
        replication_mode=ReplicationMode.SNAPSHOT,
        sync_interval_seconds=190,
        pull_batch_size=248,
        initial_load_parallelism=214,
        snapshot_num_rows_per_partition=1000,
        snapshot_number_of_parallel_tables=16,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

