
# V1 Organizations Udfs Attachments Service Id Response 2

## Structure

`V1OrganizationsUdfsAttachmentsServiceIdResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |

## Example

```python
from openapispecforclickhousecloud.models.v_1_organizations_udfs_attachments_service_id_response_2 import V1OrganizationsUdfsAttachmentsServiceIdResponse2

v_1_organizations_udfs_attachments_service_id_response_2 = V1OrganizationsUdfsAttachmentsServiceIdResponse2(
    status=200,
    request_id='00001524-0000-0000-0000-000000000000'
)
```

