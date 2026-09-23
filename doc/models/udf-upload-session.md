
# Udf Upload Session

## Structure

`UdfUploadSession`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upload_id` | `uuid\|str` | Required | Identifier of the uploaded source archive. |
| `upload_url` | `str` | Required | Presigned URL for uploading the source archive. |
| `expires_at` | `datetime` | Required | Presigned-URL expiry timestamp. |

## Example

```python
import dateutil.parser

from openapispecforclickhousecloud.models.udf_upload_session import UdfUploadSession

udf_upload_session = UdfUploadSession(
    upload_id='00000a2c-0000-0000-0000-000000000000',
    upload_url='uploadUrl2',
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

