
# Click Pipe Patch Kinesis Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePatchKinesisSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication` | [`Authentication5`](../../doc/models/authentication-5.md) | Optional | Authentication method to use with the Kinesis stream. |
| `iam_role` | `str` | Optional | IAM role to use for authentication. Required if IAM_ROLE is used. |
| `access_key` | [`MskIamUser`](../../doc/models/msk-iam-user.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.authentication_5 import Authentication5
from openapispecforclickhousecloud.models.click_pipe_patch_kinesis_source import ClickPipePatchKinesisSource
from openapispecforclickhousecloud.models.msk_iam_user import MskIamUser

click_pipe_patch_kinesis_source = ClickPipePatchKinesisSource(
    authentication=Authentication5.IAM_ROLE,
    iam_role='arn:aws:iam::123456789012:role/MyRole',
    access_key=MskIamUser(
        access_key_id='accessKeyId8',
        secret_key='secretKey6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

