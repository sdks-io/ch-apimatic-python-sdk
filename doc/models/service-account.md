
# Service Account

*This model accepts additional fields of type Any.*

## Structure

`ServiceAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_account_file` | `str` | Required | Google Cloud service account JSON key file content, base64 encoded. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_account import ServiceAccount

service_account = ServiceAccount(
    service_account_file='serviceAccountFile2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

