
# Click Pipe Post Kinesis Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipePostKinesisSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `format` | [`Format2`](../../doc/models/format-2.md) | Optional | Format of the Kinesis stream. |
| `stream_name` | `str` | Optional | Name of the Kinesis stream. |
| `region` | `str` | Optional | AWS region of the Kinesis stream. |
| `use_enhanced_fan_out` | `bool` | Optional | Use enhanced fan-out for the Kinesis stream. |
| `iterator_type` | [`IteratorType`](../../doc/models/iterator-type.md) | Optional | Type of iterator to use when reading from the Kinesis stream. If AT_TIMESTAMP is used, the timestamp field must be provided. |
| `timestamp` | `int` | Optional | UNIX timestamp to start reading from the Kinesis stream. Required if iteratorType is AT_TIMESTAMP. |
| `authentication` | [`Authentication5`](../../doc/models/authentication-5.md) | Optional | Authentication method to use with the Kinesis stream. |
| `iam_role` | `str` | Optional | IAM role to use for authentication. Required if IAM_ROLE is used. |
| `access_key` | [`MskIamUser`](../../doc/models/msk-iam-user.md) | Optional | - |
| `protobuf_schema` | `str` | Optional | Base64-encoded .proto source or serialized FileDescriptorSet. Required with Protobuf format and not supported with other formats.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1048576` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_post_kinesis_source import ClickPipePostKinesisSource
from openapispecforclickhousecloud.models.format_2 import Format2
from openapispecforclickhousecloud.models.iterator_type import IteratorType

click_pipe_post_kinesis_source = ClickPipePostKinesisSource(
    format=Format2.JSONEACHROW,
    stream_name='my-stream',
    region='us-east-1',
    use_enhanced_fan_out=False,
    iterator_type=IteratorType.AT_TIMESTAMP,
    timestamp=1615766400,
    iam_role='arn:aws:iam::123456789012:role/MyRole',
    protobuf_schema='c3ludGF4ID0gInByb3RvMyI7IG1lc3NhZ2UgRXZlbnQge30=',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

