
# Udf Attachment

## Structure

`UdfAttachment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `function_name` | `str` | Required | Name of the UDF. |
| `service_id` | `uuid\|str` | Required | ID of the attached service. |
| `status` | [`Status3`](../../doc/models/status-3.md) | Required | Current attachment lifecycle state. |
| `version` | `int` | Required | Attached UDF version.<br><br>**Constraints**: `>= 1` |

## Example

```python
from openapispecforclickhousecloud.models.status_3 import Status3
from openapispecforclickhousecloud.models.udf_attachment import UdfAttachment

udf_attachment = UdfAttachment(
    function_name='functionName6',
    service_id='00002698-0000-0000-0000-000000000000',
    status=Status3.PROVISIONING,
    version=1
)
```

