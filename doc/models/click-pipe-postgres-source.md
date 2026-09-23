
# Click Pipe Postgres Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostgresSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type7`](../../doc/models/type-7.md) | Optional | Type of the Postgres source. Defaults to "postgres" if not specified. |
| `host` | `str` | Optional | PostgreSQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here. |
| `port` | `int` | Optional | PostgreSQL server port.<br><br>**Constraints**: `>= 1`, `<= 65535` |
| `database` | `str` | Optional | PostgreSQL database name to replicate from. |
| `authentication` | [`Authentication11`](../../doc/models/authentication-11.md) | Optional | Authentication method for Postgres connection. |
| `iam_role` | `str` | Optional | IAM role ARN for IAM authentication (required for IAM_ROLE authentication). |
| `tls_host` | `str` | Optional | TLS/SSL host for secure connections. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificate to validate the Postgres server certificate. |
| `disable_tls` | `bool` | Optional | Disable TLS for the Postgres connection. Use with caution in production environments. |
| `skip_cert_verification` | `bool` | Optional | Skip TLS certificate verification for the Postgres connection. Use with caution in production environments. |
| `settings` | [`ClickPipePostgresPipeSettings`](../../doc/models/click-pipe-postgres-pipe-settings.md) | Optional | - |
| `table_mappings` | [`List[ClickPipePostgresPipeTableMapping]`](../../doc/models/click-pipe-postgres-pipe-table-mapping.md) | Optional | List of table mappings defining which PostgreSQL tables to replicate and how they map to ClickHouse tables. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_11 import Authentication11
from openapispecforclickhousecloud.models.click_pipe_postgres_source import ClickPipePostgresSource
from openapispecforclickhousecloud.models.type_7 import Type7

click_pipe_postgres_source = ClickPipePostgresSource(
    mtype=Type7.POSTGRES,
    host='my-postgres-server.example.com',
    port=5432,
    database='production_db',
    authentication=Authentication11.IAM_ROLE,
    iam_role='arn:aws:iam::123456789012:role/MyApplicationRole',
    tls_host='my-postgres-server.example.com',
    ca_certificate='-----BEGIN CERTIFICATE-----\n...',
    disable_tls=False,
    skip_cert_verification=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

