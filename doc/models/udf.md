
# Udf

## Structure

`Udf`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `function_name` | `str` | Required | Name of the UDF. Unique within the organization. |
| `version` | `int` | Required | Version number of the UDF.<br><br>**Constraints**: `>= 1` |
| `status` | [`Status4`](../../doc/models/status-4.md) | Required | Build state of this UDF version. |
| `runtime` | [`Runtime4`](../../doc/models/runtime-4.md) | Required | Runtime used to execute the UDF command. |
| `mtype` | [`Type22`](../../doc/models/type-22.md) | Required | Executable UDF type. |
| `arguments` | [`List[UdfArgumentOutput]`](../../doc/models/udf-argument-output.md) | Required | Arguments passed to the UDF command. |
| `return_type` | `str` | Required | ClickHouse data type of the returned value. |
| `return_name` | str | Required | This is a container for any-of cases. |
| `pool_size` | int | Required | This is a container for any-of cases. |
| `command_read_timeout` | `int` | Required | Command stdout read timeout in milliseconds.<br><br>**Constraints**: `>= 1` |
| `command_write_timeout` | `int` | Required | Command stdin write timeout in milliseconds.<br><br>**Constraints**: `>= 1` |
| `max_command_execution_time` | int | Required | This is a container for any-of cases. |
| `memory_limit_mib` | int | Required | This is a container for any-of cases. |
| `send_chunk_header` | `bool` | Required | Whether ClickHouse sends a row-count chunk header. |
| `deterministic` | `bool` | Required | Whether ClickHouse may reuse cached query results for this UDF. |
| `format` | `str` | Required | Input and output format used by the UDF command. |
| `sandbox_type` | [`SandboxType4`](../../doc/models/sandbox-type-4.md) | Required | Sandbox isolation level. |
| `sandbox_version` | [`SandboxVersion4`](../../doc/models/sandbox-version-4.md) | Required | Sandbox runtime version. |
| `error` | str | Required | This is a container for any-of cases. |
| `created_at` | `datetime` | Required | Creation timestamp. |
| `updated_at` | `datetime` | Required | Last-update timestamp. |

## Example

```python
import dateutil.parser

from openapispecforclickhousecloud.models.runtime_4 import Runtime4
from openapispecforclickhousecloud.models.sandbox_type_4 import SandboxType4
from openapispecforclickhousecloud.models.sandbox_version_4 import SandboxVersion4
from openapispecforclickhousecloud.models.status_4 import Status4
from openapispecforclickhousecloud.models.type_22 import Type22
from openapispecforclickhousecloud.models.udf import Udf
from openapispecforclickhousecloud.models.udf_argument_output import UdfArgumentOutput

udf = Udf(
    function_name='functionName2',
    version=1,
    status=Status4.READY,
    runtime=Runtime4.ENUM_PYTHON311,
    mtype=Type22.EXECUTABLE,
    arguments=[
        UdfArgumentOutput(
            name='name8',
            mtype='type2'
        )
    ],
    return_type='returnType2',
    return_name='String7',
    pool_size=222,
    command_read_timeout=216,
    command_write_timeout=162,
    max_command_execution_time=112,
    memory_limit_mib=None,
    send_chunk_header=False,
    deterministic=False,
    format='format0',
    sandbox_type=SandboxType4.BASIC,
    sandbox_version=SandboxVersion4.V3,
    error='String9',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

