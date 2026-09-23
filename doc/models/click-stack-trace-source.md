
# Click Stack Trace Source

*This model accepts additional fields of type Any.*

## Structure

`ClickStackTraceSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique source ID. Server-generated; ignored if sent in create/update requests. |
| `name` | `str` | Required | Display name for the source. |
| `section` | `str` | Optional | Optional grouping label used to organize sources in the source selector. Sources that share a section value are displayed together. |
| `disabled` | `bool` | Optional | When true, the source is hidden from source selectors in the UI. Defaults to false. |
| `kind` | `str` | Required, Constant | Source kind discriminator. Must be "trace" for trace sources.<br><br>**Value**: `"trace"` |
| `connection` | `str` | Required | ID of the ClickHouse connection used by this source. |
| `mfrom` | [`ClickStackSourceFrom`](../../doc/models/click-stack-source-from.md) | Required | - |
| `query_settings` | [`List[ClickStackQuerySetting]`](../../doc/models/click-stack-query-setting.md) | Optional | Optional ClickHouse query settings applied when querying this source. |
| `filter_settings` | [`ClickStackSourceFilterSettings`](../../doc/models/click-stack-source-filter-settings.md) | Optional | - |
| `default_table_select_expression` | `str` | Required | Default columns selected in search results (this can be customized per search later) |
| `timestamp_value_expression` | `str` | Required | DateTime column or expression defines the start of the span |
| `duration_expression` | `str` | Required | Expression to extract span duration. |
| `duration_precision` | `int` | Required | Number of decimal digits in the duration value (e.g., 3 for milliseconds, 6 for microseconds, 9 for nanoseconds). |
| `trace_id_expression` | `str` | Required | Expression to extract the trace ID. |
| `span_id_expression` | `str` | Required | Expression to extract the span ID. |
| `parent_span_id_expression` | `str` | Required | Expression to extract the parent span ID. |
| `span_name_expression` | `str` | Required | Expression to extract the span name. |
| `span_kind_expression` | `str` | Required | Expression to extract the span kind (e.g., client, server, internal). |
| `log_source_id` | `str` | Optional | HyperDX Source for logs associated with traces. Optional |
| `session_source_id` | `str` | Optional | HyperDX Source for sessions associated with traces. Optional |
| `metric_source_id` | `str` | Optional | HyperDX Source for metrics associated with traces. Optional |
| `status_code_expression` | `str` | Optional | Expression to extract the span status code. |
| `status_message_expression` | `str` | Optional | Expression to extract the span status message. |
| `service_name_expression` | `str` | Optional | Expression to extract the service name from trace rows. |
| `service_version_expression` | `str` | Optional | Expression identifying the running release of a service. Defaults to the OpenTelemetry service.version resource attribute when unset. Where services carry the release on different attributes, fall back across them with coalesce(nullIf(a, ''), nullIf(b, '')). |
| `resource_attributes_expression` | `str` | Optional | Expression to extract resource-level attributes. |
| `event_attributes_expression` | `str` | Optional | Expression to extract event-level attributes. |
| `span_events_value_expression` | `str` | Optional | Expression to extract span events. Used to capture events associated with spans. Expected to be Nested ( Timestamp DateTime64(9), Name LowCardinality(String), Attributes Map(LowCardinality(String), String) |
| `implicit_column_expression` | `str` | Optional | Column used for full text search if no property is specified in a Lucene-based search. Typically the message body of a log. |
| `known_columns_list_expression` | `str` | Optional | For Distributed table sources whose target tables have non-matching column sets. A list of columns supported across all target tables, used instead of SELECT * when fetching full row data. Leave blank to select all columns. |
| `use_text_index_for_implicit_column` | [`UseTextIndexForImplicitColumn`](../../doc/models/use-text-index-for-implicit-column.md) | Optional | Controls whether lucene rendering uses ClickHouse text indices via hasAllTokens() against the implicit column. "auto" detects a covering index at query time, "enabled" forces text index usage, "disabled" forces a LIKE/hasToken fallback. |
| `highlighted_trace_attribute_expressions` | [`List[ClickStackHighlightedAttributeExpression]`](../../doc/models/click-stack-highlighted-attribute-expression.md) | Optional | Expressions defining trace-level attributes which are displayed in the trace view for the selected trace. |
| `highlighted_row_attribute_expressions` | [`List[ClickStackHighlightedAttributeExpression]`](../../doc/models/click-stack-highlighted-attribute-expression.md) | Optional | Expressions defining row-level attributes which are displayed in the row side panel for the selected row |
| `materialized_views` | [`List[ClickStackMaterializedView]`](../../doc/models/click-stack-materialized-view.md) | Optional | Configure materialized views for query optimization. These pre-aggregated views can significantly improve query performance on aggregation queries. |
| `metadata_materialized_views` | [`ClickStackTraceSourceMetadataMaterializedViews`](../../doc/models/click-stack-trace-source-metadata-materialized-views.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_filter_settings_column import ClickStackFilterSettingsColumn
from openapispecforclickhousecloud.models.click_stack_query_setting import ClickStackQuerySetting
from openapispecforclickhousecloud.models.click_stack_source_filter_settings import ClickStackSourceFilterSettings
from openapispecforclickhousecloud.models.click_stack_source_from import ClickStackSourceFrom
from openapispecforclickhousecloud.models.click_stack_trace_source import ClickStackTraceSource
from openapispecforclickhousecloud.models.use_text_index_for_implicit_column import UseTextIndexForImplicitColumn

click_stack_trace_source = ClickStackTraceSource(
    name='Traces',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    default_table_select_expression='Timestamp, SpanName, ServiceName, Duration',
    timestamp_value_expression='Timestamp',
    duration_expression='Duration',
    duration_precision=92,
    trace_id_expression='TraceId',
    span_id_expression='SpanId',
    parent_span_id_expression='ParentSpanId',
    span_name_expression='SpanName',
    span_kind_expression='SpanKind',
    id='507f1f77bcf86cd799439021',
    section='Billing',
    disabled=False,
    query_settings=[
        ClickStackQuerySetting(
            setting='setting6',
            value='value0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackQuerySetting(
            setting='setting6',
            value='value0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackQuerySetting(
            setting='setting6',
            value='value0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    filter_settings=ClickStackSourceFilterSettings(
        database_name='databaseName4',
        table_name='tableName4',
        columns=[
            ClickStackFilterSettingsColumn(
                name='name0',
                label='label0',
                value_expression='valueExpression8',
                allow_all=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    log_source_id='507f1f77bcf86cd799439011',
    session_source_id='507f1f77bcf86cd799439031',
    metric_source_id='507f1f77bcf86cd799439041',
    status_code_expression='StatusCode',
    status_message_expression='StatusMessage',
    service_name_expression='ServiceName',
    service_version_expression='ResourceAttributes[\'service.version\']',
    resource_attributes_expression='ResourceAttributes',
    event_attributes_expression='SpanAttributes',
    span_events_value_expression='Events',
    implicit_column_expression='SpanName',
    known_columns_list_expression='Timestamp, Body, ServiceName',
    use_text_index_for_implicit_column=UseTextIndexForImplicitColumn.AUTO,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

