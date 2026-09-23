
# Click Pipe Patch My Sql Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchMySqlSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credentials` | [`Plain`](../../doc/models/plain.md) | Optional | - |
| `host` | `str` | Required | MySQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here. |
| `port` | `int` | Required | MySQL server port.<br><br>**Constraints**: `>= 1`, `<= 65535` |
| `authentication` | [`Authentication13`](../../doc/models/authentication-13.md) | Optional | Authentication method for MySQL connection. |
| `iam_role` | `str` | Optional | IAM role ARN for IAM authentication (required for IAM_ROLE authentication). |
| `tls_host` | `str` | Optional | TLS/SSL host for secure connections. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificate to validate the MySQL server certificate. |
| `disable_tls` | `bool` | Optional | Disable TLS for the MySQL connection. Use with caution in production environments. |
| `skip_cert_verification` | `bool` | Optional | Skip TLS certificate verification for the MySQL connection. Use with caution in production environments. |
| `server_id` | `int` | Optional | Optional MySQL server_id the pipe declares itself as in the MySQL replication topology. Must be unique across replicas connected to the source. If omitted, one is assigned automatically.<br><br>**Constraints**: `>= 1`, `<= 4294967295` |
| `settings` | [`ClickPipePatchMySqlPipeSettings`](../../doc/models/click-pipe-patch-my-sql-pipe-settings.md) | Optional | - |
| `table_mappings_to_add` | [`List[ClickPipeMySqlPipeTableMapping]`](../../doc/models/click-pipe-my-sql-pipe-table-mapping.md) | Optional | Table mappings to add to the pipe. Can be an empty array if no tables are being added.<br><br>**Constraints**: *Minimum Items*: `0` |
| `table_mappings_to_remove` | [`List[ClickPipePatchMySqlPipeRemoveTableMapping]`](../../doc/models/click-pipe-patch-my-sql-pipe-remove-table-mapping.md) | Optional | Table mappings to remove from the pipe. Only sourceSchemaName, sourceTable, and targetTable are required for removal.<br><br>**Constraints**: *Minimum Items*: `0` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_13 import Authentication13
from openapispecforclickhousecloud.models.click_pipe_patch_my_sql_source import ClickPipePatchMySqlSource
from openapispecforclickhousecloud.models.plain import Plain

click_pipe_patch_my_sql_source = ClickPipePatchMySqlSource(
    host='my-mysql-server.example.com',
    port=3306,
    credentials=Plain(
        username='username4',
        password='password0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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

