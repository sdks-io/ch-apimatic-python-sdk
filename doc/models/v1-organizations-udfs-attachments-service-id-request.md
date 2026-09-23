
# V1 Organizations Udfs Attachments Service Id Request

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsUdfsAttachmentsServiceIdRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `int` | Optional | Version to attach. When omitted, the latest ready version is attached.<br><br>**Constraints**: `>= 1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.v_1_organizations_udfs_attachments_service_id_request import V1OrganizationsUdfsAttachmentsServiceIdRequest

v_1_organizations_udfs_attachments_service_id_request = V1OrganizationsUdfsAttachmentsServiceIdRequest(
    version=1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

