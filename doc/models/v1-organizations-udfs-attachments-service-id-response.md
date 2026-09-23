
# V1 Organizations Udfs Attachments Service Id Response

## Structure

`V1OrganizationsUdfsAttachmentsServiceIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |
| `result` | [`UdfAttachment`](../../doc/models/udf-attachment.md) | Required | - |

## Example

```python
from openapispecforclickhousecloud.models.status_3 import Status3
from openapispecforclickhousecloud.models.udf_attachment import UdfAttachment
from openapispecforclickhousecloud.models.v_1_organizations_udfs_attachments_service_id_response import V1OrganizationsUdfsAttachmentsServiceIdResponse

v_1_organizations_udfs_attachments_service_id_response = V1OrganizationsUdfsAttachmentsServiceIdResponse(
    status=200,
    request_id='0000167e-0000-0000-0000-000000000000',
    result=UdfAttachment(
        function_name='functionName4',
        service_id='000011f8-0000-0000-0000-000000000000',
        status=Status3.PROVISIONING,
        version=1
    )
)
```

