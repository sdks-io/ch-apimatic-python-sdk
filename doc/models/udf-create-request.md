
# Udf Create Request

*This model accepts additional fields of type Any.*

## Structure

`UdfCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `upload_id` | `uuid\|str` | Required | Identifier of the uploaded source archive. |
| `runtime` | [`Runtime`](../../doc/models/runtime.md) | Required | - |
| `arguments` | [`List[UdfArgument]`](../../doc/models/udf-argument.md) | Required | - |
| `return_type` | `str` | Required | - |
| `return_name` | str \| None | Optional | This is a container for any-of cases. |
| `command_read_timeout` | `int` | Optional | **Default**: `10000`<br><br>**Constraints**: `>= 1` |
| `command_write_timeout` | `int` | Optional | **Default**: `10000`<br><br>**Constraints**: `>= 1` |
| `memory_limit_mib` | int \| None | Optional | This is a container for any-of cases. |
| `send_chunk_header` | `bool` | Optional | **Default**: `False` |
| `deterministic` | `bool` | Optional | Marks the UDF as deterministic so ClickHouse can reuse cached query results. Only set this when the UDF always returns the same result for the same arguments.<br><br>**Default**: `False` |
| `format` | `str` | Optional | **Default**: `"TabSeparated"` |
| `sandbox_type` | [`SandboxType`](../../doc/models/sandbox-type.md) | Optional | **Default**: `"basic"` |
| `sandbox_version` | [`SandboxVersion`](../../doc/models/sandbox-version.md) | Optional | **Default**: `"v2"` |
| `mtype` | `str` | Required, Constant | **Value**: `"executable"` |
| `pool_size` | `str` | Optional | Always null — an executable UDF has no command pool. |
| `max_command_execution_time` | int \| None | Optional | This is a container for any-of cases. |
| `function_name` | `str` | Required | **Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.runtime import Runtime
from openapispecforclickhousecloud.models.sandbox_type import SandboxType
from openapispecforclickhousecloud.models.sandbox_version import SandboxVersion
from openapispecforclickhousecloud.models.udf_argument import UdfArgument
from openapispecforclickhousecloud.models.udf_create_request import UdfCreateRequest

udf_create_request = UdfCreateRequest(
    upload_id='000000d4-0000-0000-0000-000000000000',
    runtime=Runtime.ENUM_PYTHON311,
    arguments=[
        UdfArgument(
            name='name8',
            mtype='type2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    return_type='returnType0',
    function_name='functionName0',
    return_name='String5',
    command_read_timeout=10000,
    command_write_timeout=10000,
    memory_limit_mib=104,
    send_chunk_header=False,
    deterministic=False,
    format='TabSeparated',
    sandbox_type=SandboxType.BASIC,
    sandbox_version=SandboxVersion.V2,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

