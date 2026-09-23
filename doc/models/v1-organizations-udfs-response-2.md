
# V1 Organizations Udfs Response 2

## Structure

`V1OrganizationsUdfsResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |

## Example

```python
from openapispecforclickhousecloud.models.v_1_organizations_udfs_response_2 import V1OrganizationsUdfsResponse2

v_1_organizations_udfs_response_2 = V1OrganizationsUdfsResponse2(
    status=200,
    request_id='000004c2-0000-0000-0000-000000000000'
)
```

