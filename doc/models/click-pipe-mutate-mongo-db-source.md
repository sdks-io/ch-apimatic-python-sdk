
# Click Pipe Mutate Mongo Db Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeMutateMongoDbSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credentials` | [`Plain`](../../doc/models/plain.md) | Optional | - |
| `uri` | `str` | Required | MongoDB connection URI. Supports both standard URIs (mongodb://...) and SRV URIs (mongodb+srv://...). Embedded credentials are redacted from API responses, so the returned value can differ from what was submitted. |
| `read_preference` | [`ReadPreference`](../../doc/models/read-preference.md) | Required | MongoDB read preference for replica set reads. |
| `tls_host` | `str` | Optional | TLS/SSL host for secure connections. |
| `disable_tls` | `bool` | Optional | Disable TLS for the MongoDB connection. Defaults to false (TLS enabled).<br><br>**Default**: `False` |
| `skip_cert_verification` | `bool` | Optional | Skip TLS certificate verification for the MongoDB connection. Use with caution in production environments. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificate to validate the MongoDB server certificate. |
| `settings` | [`ClickPipeMongoDbPipeSettings`](../../doc/models/click-pipe-mongo-db-pipe-settings.md) | Required | - |
| `table_mappings` | [`List[ClickPipeMongoDbPipeTableMapping]`](../../doc/models/click-pipe-mongo-db-pipe-table-mapping.md) | Required | List of collection mappings defining which MongoDB collections to replicate and how they map to ClickHouse tables. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_mongo_db_pipe_settings import ClickPipeMongoDbPipeSettings
from openapispecforclickhousecloud.models.click_pipe_mongo_db_pipe_table_mapping import ClickPipeMongoDbPipeTableMapping
from openapispecforclickhousecloud.models.click_pipe_mutate_mongo_db_source import ClickPipeMutateMongoDbSource
from openapispecforclickhousecloud.models.plain import Plain
from openapispecforclickhousecloud.models.read_preference import ReadPreference
from openapispecforclickhousecloud.models.replication_mode import ReplicationMode
from openapispecforclickhousecloud.models.table_engine import TableEngine

click_pipe_mutate_mongo_db_source = ClickPipeMutateMongoDbSource(
    uri='mongodb+srv://cluster0.example.mongodb.net/mydb',
    read_preference=ReadPreference.SECONDARYPREFERRED,
    settings=ClickPipeMongoDbPipeSettings(
        replication_mode=ReplicationMode.CDC,
        sync_interval_seconds=60,
        pull_batch_size=100000,
        initial_load_parallelism=1,
        snapshot_num_rows_per_partition=100000,
        snapshot_number_of_parallel_tables=1,
        delete_on_merge=False,
        use_json_native_format=True,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    table_mappings=[
        ClickPipeMongoDbPipeTableMapping(
            source_database_name='mydb',
            source_collection='users',
            target_table='mydb_users',
            table_engine=TableEngine.REPLACINGMERGETREE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    credentials=Plain(
        username='username4',
        password='password0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    tls_host='cluster0.example.mongodb.net',
    disable_tls=False,
    skip_cert_verification=False,
    ca_certificate='-----BEGIN CERTIFICATE-----\n...',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

