
# Click Pipe Patch Mongo Db Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchMongoDbSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credentials` | [`Plain`](../../doc/models/plain.md) | Optional | - |
| `uri` | `str` | Required | MongoDB connection URI (mongodb:// or mongodb+srv://). Credentials are redacted in responses; a masked value is never saved as a credential, so a real credential equal to [REDACTED] cannot be set. To change the connection, send the full URI with real credentials; omit this field or resend the redacted value to leave it unchanged. |
| `read_preference` | [`ReadPreference`](../../doc/models/read-preference.md) | Required | MongoDB read preference for replica set reads. |
| `tls_host` | `str` | Optional | TLS/SSL host for secure connections. |
| `disable_tls` | `bool` | Optional | Disable TLS for the MongoDB connection. Defaults to false (TLS enabled). |
| `skip_cert_verification` | `bool` | Optional | Skip TLS certificate verification for the MongoDB connection. Use with caution in production environments. |
| `ca_certificate` | `str` | Optional | PEM encoded CA certificate to validate the MongoDB server certificate. |
| `settings` | [`ClickPipePatchMongoDbPipeSettings`](../../doc/models/click-pipe-patch-mongo-db-pipe-settings.md) | Optional | - |
| `table_mappings_to_add` | [`List[ClickPipeMongoDbPipeTableMapping]`](../../doc/models/click-pipe-mongo-db-pipe-table-mapping.md) | Optional | Collection mappings to add to the pipe. Can be an empty array if no collections are being added.<br><br>**Constraints**: *Minimum Items*: `0` |
| `table_mappings_to_remove` | [`List[ClickPipePatchMongoDbPipeRemoveTableMapping]`](../../doc/models/click-pipe-patch-mongo-db-pipe-remove-table-mapping.md) | Optional | Collection mappings to remove from the pipe. Only sourceDatabaseName, sourceCollection, and targetTable are required for removal.<br><br>**Constraints**: *Minimum Items*: `0` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_patch_mongo_db_source import ClickPipePatchMongoDbSource
from openapispecforclickhousecloud.models.plain import Plain
from openapispecforclickhousecloud.models.read_preference import ReadPreference

click_pipe_patch_mongo_db_source = ClickPipePatchMongoDbSource(
    uri='mongodb+srv://cluster0.example.mongodb.net/mydb',
    read_preference=ReadPreference.SECONDARYPREFERRED,
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

