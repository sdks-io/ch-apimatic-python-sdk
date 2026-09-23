
# Udf Version List Response

## Structure

`UdfVersionListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[Udf]`](../../doc/models/udf.md) | Required | - |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Required | - |

## Example

```python
import dateutil.parser

from openapispecforclickhousecloud.models.pagination import Pagination
from openapispecforclickhousecloud.models.runtime_4 import Runtime4
from openapispecforclickhousecloud.models.sandbox_type_4 import SandboxType4
from openapispecforclickhousecloud.models.sandbox_version_4 import SandboxVersion4
from openapispecforclickhousecloud.models.status_4 import Status4
from openapispecforclickhousecloud.models.type_22 import Type22
from openapispecforclickhousecloud.models.udf import Udf
from openapispecforclickhousecloud.models.udf_argument_output import UdfArgumentOutput
from openapispecforclickhousecloud.models.udf_version_list_response import UdfVersionListResponse

udf_version_list_response = UdfVersionListResponse(
    items=[
        Udf(
            function_name='functionName4',
            version=1,
            status=Status4.ERROR,
            runtime=Runtime4.ENUM_PYTHON311,
            mtype=Type22.EXECUTABLE,
            arguments=[
                UdfArgumentOutput(
                    name='name8',
                    mtype='type2'
                )
            ],
            return_type='returnType4',
            return_name='String1',
            pool_size=92,
            command_read_timeout=86,
            command_write_timeout=32,
            max_command_execution_time=238,
            memory_limit_mib=None,
            send_chunk_header=False,
            deterministic=False,
            format='format6',
            sandbox_type=SandboxType4.BASIC,
            sandbox_version=SandboxVersion4.V2,
            error='String3',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    pagination=Pagination(
        total_records=72,
        current_cursor='String5',
        next_cursor='String1',
        limit=80
    )
)
```

