
# V1 Organizations Udf Uploads Url Response

## Structure

`V1OrganizationsUdfUploadsUrlResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |
| `result` | [`UdfUploadSession`](../../doc/models/udf-upload-session.md) | Required | - |

## Example

```python
import dateutil.parser

from openapispecforclickhousecloud.models.udf_upload_session import UdfUploadSession
from openapispecforclickhousecloud.models.v_1_organizations_udf_uploads_url_response import V1OrganizationsUdfUploadsUrlResponse

v_1_organizations_udf_uploads_url_response = V1OrganizationsUdfUploadsUrlResponse(
    status=201,
    request_id='00001ce8-0000-0000-0000-000000000000',
    result=UdfUploadSession(
        upload_id='0000252c-0000-0000-0000-000000000000',
        upload_url='uploadUrl2',
        expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

