
# Click Stack Source

## Data Type

`ClickStackLogSource | ClickStackTraceSource | ClickStackMetricSource | ClickStackSessionSource | ClickStackPromqlSource`

## Cases

| Type |
|  --- |
| [`ClickStackLogSource`](../../../doc/models/click-stack-log-source.md) |
| [`ClickStackTraceSource`](../../../doc/models/click-stack-trace-source.md) |
| [`ClickStackMetricSource`](../../../doc/models/click-stack-metric-source.md) |
| [`ClickStackSessionSource`](../../../doc/models/click-stack-session-source.md) |
| [`ClickStackPromqlSource`](../../../doc/models/click-stack-promql-source.md) |

## ClickStackLogSource

### Initialization Code

#### Example

```python
value = ClickStackLogSource(
    name='Logs',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs'
    ),
    default_table_select_expression='Timestamp, ServiceName, SeverityText, Body',
    timestamp_value_expression='Timestamp',
    id='507f1f77bcf86cd799439011',
    section='Billing',
    disabled=False,
    service_name_expression='ServiceName',
    service_version_expression='ResourceAttributes[\'service.version\']',
    severity_text_expression='SeverityText',
    body_expression='Body',
    event_attributes_expression='LogAttributes',
    resource_attributes_expression='ResourceAttributes',
    displayed_timestamp_value_expression='TimestampTime',
    metric_source_id='507f1f77bcf86cd799439013',
    trace_source_id='507f1f77bcf86cd799439014',
    trace_id_expression='TraceId',
    span_id_expression='SpanId',
    implicit_column_expression='Body',
    known_columns_list_expression='Timestamp, Body, ServiceName',
    use_text_index_for_implicit_column=UseTextIndexForImplicitColumn.AUTO
)
```

## ClickStackTraceSource

### Initialization Code

#### Example

```python
value = ClickStackTraceSource(
    name='Traces',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs'
    ),
    default_table_select_expression='Timestamp, SpanName, ServiceName, Duration',
    timestamp_value_expression='Timestamp',
    duration_expression='Duration',
    duration_precision=2,
    trace_id_expression='TraceId',
    span_id_expression='SpanId',
    parent_span_id_expression='ParentSpanId',
    span_name_expression='SpanName',
    span_kind_expression='SpanKind',
    id='507f1f77bcf86cd799439021',
    section='Billing',
    disabled=False,
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
    use_text_index_for_implicit_column=UseTextIndexForImplicitColumn.AUTO
)
```

## ClickStackMetricSource

### Initialization Code

#### Example

```python
value = ClickStackMetricSource(
    name='Metrics',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackMetricSourceFrom(
        database_name='otel',
        table_name='otel_metrics_gauge'
    ),
    metric_tables=ClickStackMetricTables(
        gauge='otel_metrics_gauge',
        histogram='otel_metrics_histogram',
        sum='otel_metrics_sum',
        summary='otel_metrics_summary',
        exponential_histogram='otel_metrics_exponential_histogram'
    ),
    timestamp_value_expression='TimeUnix',
    resource_attributes_expression='ResourceAttributes',
    id='507f1f77bcf86cd799439041',
    section='Billing',
    disabled=False,
    log_source_id='507f1f77bcf86cd799439011'
)
```

## ClickStackSessionSource

### Initialization Code

#### Example

```python
value = ClickStackSessionSource(
    name='Sessions',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs'
    ),
    trace_source_id='507f1f77bcf86cd799439021',
    id='507f1f77bcf86cd799439031',
    section='Billing',
    disabled=False,
    timestamp_value_expression='TimestampTime'
)
```

## ClickStackPromqlSource

### Initialization Code

#### Example

```python
value = ClickStackPromqlSource(
    name='Prometheus Metrics',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs'
    ),
    timestamp_value_expression='timestamp',
    id='507f1f77bcf86cd799439051',
    section='Billing',
    disabled=False
)
```

