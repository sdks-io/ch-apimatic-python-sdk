
# V1 Organizations Udfs Versions Version Response

## Structure

`V1OrganizationsUdfsVersionsVersionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |

## Example

```python
from openapispecforclickhousecloud.models.v_1_organizations_udfs_versions_version_response import V1OrganizationsUdfsVersionsVersionResponse

v_1_organizations_udfs_versions_version_response = V1OrganizationsUdfsVersionsVersionResponse(
    status=200,
    request_id='000008e4-0000-0000-0000-000000000000'
)
```

