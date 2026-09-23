
# Click Pipe Destination Table Engine

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeDestinationTableEngine`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type11`](../../doc/models/type-11.md) | Optional | Engine type of the destination table. |
| `version_column_id` | `str` | Optional | Column name to use as version for ReplacingMergeTree engine. |
| `column_ids` | `List[str]` | Optional | Column names to sum for SummingMergeTree engine. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_destination_table_engine import ClickPipeDestinationTableEngine
from openapispecforclickhousecloud.models.type_11 import Type11

click_pipe_destination_table_engine = ClickPipeDestinationTableEngine(
    mtype=Type11.MERGETREE,
    version_column_id='versionColumnId4',
    column_ids=[
        'columnIds0',
        'columnIds9'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

