
# V1 Organizations Udfs Attachments Response

## Structure

`V1OrganizationsUdfsAttachmentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |
| `result` | [`UdfAttachmentListResponse`](../../doc/models/udf-attachment-list-response.md) | Required | - |

## Example

```python
from openapispecforclickhousecloud.models.pagination import Pagination
from openapispecforclickhousecloud.models.status_3 import Status3
from openapispecforclickhousecloud.models.udf_attachment import UdfAttachment
from openapispecforclickhousecloud.models.udf_attachment_list_response import UdfAttachmentListResponse
from openapispecforclickhousecloud.models.v_1_organizations_udfs_attachments_response import V1OrganizationsUdfsAttachmentsResponse

v_1_organizations_udfs_attachments_response = V1OrganizationsUdfsAttachmentsResponse(
    status=200,
    request_id='00000382-0000-0000-0000-000000000000',
    result=UdfAttachmentListResponse(
        items=[
            UdfAttachment(
                function_name='functionName4',
                service_id='00001362-0000-0000-0000-000000000000',
                status=Status3.DEPLOYED,
                version=1
            )
        ],
        pagination=Pagination(
            total_records=72,
            current_cursor='String5',
            next_cursor='String1',
            limit=80
        )
    )
)
```

