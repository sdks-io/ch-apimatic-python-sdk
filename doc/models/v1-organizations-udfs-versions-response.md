
# V1 Organizations Udfs Versions Response

## Structure

`V1OrganizationsUdfsVersionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |
| `result` | [`Udf`](../../doc/models/udf.md) | Required | - |

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
from openapispecforclickhousecloud.models.v_1_organizations_udfs_versions_response import V1OrganizationsUdfsVersionsResponse

v_1_organizations_udfs_versions_response = V1OrganizationsUdfsVersionsResponse(
    status=201,
    request_id='00001750-0000-0000-0000-000000000000',
    result=Udf(
        function_name='functionName4',
        version=1,
        status=Status4.BUILDING,
        runtime=Runtime4.ENUM_PYTHON311,
        mtype=Type22.EXECUTABLE,
        arguments=[
            UdfArgumentOutput(
                name='name8',
                mtype='type2'
            )
        ],
        return_type='returnType4',
        return_name='String9',
        pool_size=34,
        command_read_timeout=28,
        command_write_timeout=230,
        max_command_execution_time=180,
        memory_limit_mib=None,
        send_chunk_header=False,
        deterministic=False,
        format='format2',
        sandbox_type=SandboxType4.BASIC,
        sandbox_version=SandboxVersion4.V1,
        error='String1',
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

