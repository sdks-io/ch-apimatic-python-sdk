
# Click Stack Session Source

*This model accepts additional fields of type Any.*

## Structure

`ClickStackSessionSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique source ID. Server-generated; ignored if sent in create/update requests. |
| `name` | `str` | Required | Display name for the source. |
| `section` | `str` | Optional | Optional grouping label used to organize sources in the source selector. Sources that share a section value are displayed together. |
| `disabled` | `bool` | Optional | When true, the source is hidden from source selectors in the UI. Defaults to false. |
| `kind` | `str` | Required, Constant | Source kind discriminator. Must be "session" for session sources.<br><br>**Value**: `"session"` |
| `connection` | `str` | Required | ID of the ClickHouse connection used by this source. |
| `mfrom` | [`ClickStackSourceFrom`](../../doc/models/click-stack-source-from.md) | Required | - |
| `query_settings` | [`List[ClickStackQuerySetting]`](../../doc/models/click-stack-query-setting.md) | Optional | Optional ClickHouse query settings applied when querying this source. |
| `timestamp_value_expression` | `str` | Optional | DateTime column or expression that is part of your table's primary key. |
| `trace_source_id` | `str` | Required | HyperDX Source for traces associated with sessions. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_query_setting import ClickStackQuerySetting
from openapispecforclickhousecloud.models.click_stack_session_source import ClickStackSessionSource
from openapispecforclickhousecloud.models.click_stack_source_from import ClickStackSourceFrom

click_stack_session_source = ClickStackSessionSource(
    name='Sessions',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    trace_source_id='507f1f77bcf86cd799439021',
    id='507f1f77bcf86cd799439031',
    section='Billing',
    disabled=False,
    query_settings=[
        ClickStackQuerySetting(
            setting='setting6',
            value='value0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    timestamp_value_expression='TimestampTime',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

