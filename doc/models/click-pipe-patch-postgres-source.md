
# Click Pipe Patch Postgres Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchPostgresSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credentials` | [`Plain`](../../doc/models/plain.md) | Optional | - |
| `host` | `str` | Optional | PostgreSQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here. |
| `port` | `int` | Optional | PostgreSQL server port.<br><br>**Constraints**: `>= 1`, `<= 65535` |
| `database` | `str` | Optional | PostgreSQL database name to replicate from. |
| `tls_host` | `str` | Optional | TLS/SSL host for secure connections. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificate to validate the Postgres server certificate. |
| `disable_tls` | `bool` | Optional | Disable TLS for the Postgres connection. Use with caution in production environments. |
| `skip_cert_verification` | `bool` | Optional | Skip TLS certificate verification for the Postgres connection. Use with caution in production environments. |
| `settings` | [`ClickPipePatchPostgresPipeSettings`](../../doc/models/click-pipe-patch-postgres-pipe-settings.md) | Optional | - |
| `table_mappings_to_add` | [`List[ClickPipePostgresPipeTableMapping]`](../../doc/models/click-pipe-postgres-pipe-table-mapping.md) | Optional | Table mappings to add to the pipe. Can be an empty array if no tables are being added.<br><br>**Constraints**: *Minimum Items*: `0` |
| `table_mappings_to_remove` | [`List[ClickPipePatchPostgresPipeRemoveTableMapping]`](../../doc/models/click-pipe-patch-postgres-pipe-remove-table-mapping.md) | Optional | Table mappings to remove from the pipe. Only sourceSchemaName, sourceTable, and targetTable are required for removal.<br><br>**Constraints**: *Minimum Items*: `0` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_patch_postgres_source import ClickPipePatchPostgresSource
from openapispecforclickhousecloud.models.plain import Plain

click_pipe_patch_postgres_source = ClickPipePatchPostgresSource(
    credentials=Plain(
        username='username4',
        password='password0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    host='my-postgres-server.example.com',
    port=5432,
    database='production_db',
    tls_host='my-postgres-server.example.com',
    ca_certificate='-----BEGIN CERTIFICATE-----\n...',
    disable_tls=False,
    skip_cert_verification=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

