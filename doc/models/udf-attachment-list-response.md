
# Udf Attachment List Response

## Structure

`UdfAttachmentListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[UdfAttachment]`](../../doc/models/udf-attachment.md) | Required | - |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Required | - |

## Example

```python
from openapispecforclickhousecloud.models.pagination import Pagination
from openapispecforclickhousecloud.models.status_3 import Status3
from openapispecforclickhousecloud.models.udf_attachment import UdfAttachment
from openapispecforclickhousecloud.models.udf_attachment_list_response import UdfAttachmentListResponse

udf_attachment_list_response = UdfAttachmentListResponse(
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
```

