
# Msk Iam User

*This model accepts additional fields of type Any.*

## Structure

`MskIamUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_key_id` | `str` | Optional | IAM access key ID. |
| `secret_key` | `str` | Optional | IAM secret key. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.msk_iam_user import MskIamUser

msk_iam_user = MskIamUser(
    access_key_id='accessKeyId0',
    secret_key='secretKey8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

