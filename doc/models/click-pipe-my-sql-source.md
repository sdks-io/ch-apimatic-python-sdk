
# Click Pipe My Sql Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeMySqlSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type9`](../../doc/models/type-9.md) | Optional | Type of the MySQL source. Defaults to "mysql" if not specified. |
| `host` | `str` | Required | MySQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here. |
| `port` | `int` | Required | MySQL server port.<br><br>**Constraints**: `>= 1`, `<= 65535` |
| `authentication` | [`Authentication13`](../../doc/models/authentication-13.md) | Optional | Authentication method for MySQL connection. |
| `iam_role` | `str` | Optional | IAM role ARN for IAM authentication (required for IAM_ROLE authentication). |
| `tls_host` | `str` | Optional | TLS/SSL host for secure connections. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificate to validate the MySQL server certificate. |
| `disable_tls` | `bool` | Optional | Disable TLS for the MySQL connection. Use with caution in production environments. |
| `skip_cert_verification` | `bool` | Optional | Skip TLS certificate verification for the MySQL connection. Use with caution in production environments. |
| `server_id` | `int` | Optional | Optional MySQL server_id the pipe declares itself as in the MySQL replication topology. Must be unique across replicas connected to the source. If omitted, one is assigned automatically.<br><br>**Constraints**: `>= 1`, `<= 4294967295` |
| `settings` | [`ClickPipeMySqlPipeSettings`](../../doc/models/click-pipe-my-sql-pipe-settings.md) | Required | - |
| `table_mappings` | [`List[ClickPipeMySqlPipeTableMapping]`](../../doc/models/click-pipe-my-sql-pipe-table-mapping.md) | Required | List of table mappings defining which MySQL tables to replicate and how they map to ClickHouse tables. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_13 import Authentication13
from openapispecforclickhousecloud.models.click_pipe_my_sql_pipe_settings import ClickPipeMySqlPipeSettings
from openapispecforclickhousecloud.models.click_pipe_my_sql_pipe_table_mapping import ClickPipeMySqlPipeTableMapping
from openapispecforclickhousecloud.models.click_pipe_my_sql_source import ClickPipeMySqlSource
from openapispecforclickhousecloud.models.replication_mechanism import ReplicationMechanism
from openapispecforclickhousecloud.models.replication_mode import ReplicationMode
from openapispecforclickhousecloud.models.table_engine import TableEngine
from openapispecforclickhousecloud.models.type_9 import Type9

click_pipe_my_sql_source = ClickPipeMySqlSource(
    host='my-mysql-server.example.com',
    port=3306,
    settings=ClickPipeMySqlPipeSettings(
        replication_mode=ReplicationMode.CDC,
        sync_interval_seconds=60,
        pull_batch_size=1000,
        replication_mechanism=ReplicationMechanism.GTID,
        use_compression=False,
        allow_nullable_columns=False,
        initial_load_parallelism=1,
        snapshot_num_rows_per_partition=100000,
        snapshot_number_of_parallel_tables=1,
        delete_on_merge=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    table_mappings=[
        ClickPipeMySqlPipeTableMapping(
            source_schema_name='my_database',
            source_table='users',
            target_table='my_database_users',
            excluded_columns=[
                'internal_id',
                'temp_data'
            ],
            use_custom_sorting_key=False,
            sorting_keys=[
                'created_at_date',
                'event_id'
            ],
            table_engine=TableEngine.REPLACINGMERGETREE,
            partition_key='id',
            partition_by_expr='toYYYYMM(created_at)',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    mtype=Type9.AURORAMYSQL,
    authentication=Authentication13.BASIC,
    iam_role='arn:aws:iam::123456789012:role/MyApplicationRole',
    tls_host='my-mysql-server.example.com',
    ca_certificate='-----BEGIN CERTIFICATE-----\n...',
    disable_tls=False,
    skip_cert_verification=False,
    server_id=4242,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

