
# Click Stack Promql Source

*This model accepts additional fields of type Any.*

## Structure

`ClickStackPromqlSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique source ID. Server-generated; ignored if sent in create/update requests. |
| `name` | `str` | Required | Display name for the source. |
| `section` | `str` | Optional | Optional grouping label used to organize sources in the source selector. Sources that share a section value are displayed together. |
| `disabled` | `bool` | Optional | When true, the source is hidden from source selectors in the UI. Defaults to false. |
| `kind` | `str` | Required, Constant | Source kind discriminator. Must be "promql" for PromQL sources.<br><br>**Value**: `"promql"` |
| `connection` | `str` | Required | ID of the connection used by this source. Should reference a Prometheus-compatible connection. |
| `mfrom` | [`ClickStackSourceFrom`](../../doc/models/click-stack-source-from.md) | Required | - |
| `query_settings` | [`List[ClickStackQuerySetting]`](../../doc/models/click-stack-query-setting.md) | Optional | Optional ClickHouse query settings applied when querying this source. |
| `timestamp_value_expression` | `str` | Required | Required by the API for all source kinds; not used when querying a Prometheus endpoint. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_promql_source import ClickStackPromqlSource
from openapispecforclickhousecloud.models.click_stack_query_setting import ClickStackQuerySetting
from openapispecforclickhousecloud.models.click_stack_source_from import ClickStackSourceFrom

click_stack_promql_source = ClickStackPromqlSource(
    name='Prometheus Metrics',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    timestamp_value_expression='timestamp',
    id='507f1f77bcf86cd799439051',
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

