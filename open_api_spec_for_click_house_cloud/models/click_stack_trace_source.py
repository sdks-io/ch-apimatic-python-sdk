from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_stack_highlighted_attribute_expression import (
    ClickStackHighlightedAttributeExpression,
    ClickStackHighlightedAttributeExpressionDict,
)
from .click_stack_materialized_view import ClickStackMaterializedView, ClickStackMaterializedViewDict
from .click_stack_query_setting import ClickStackQuerySetting, ClickStackQuerySettingDict
from .click_stack_source_filter_settings import ClickStackSourceFilterSettings, ClickStackSourceFilterSettingsDict
from .click_stack_source_from import ClickStackSourceFrom, ClickStackSourceFromDict
from .click_stack_trace_source_metadata_materialized_views import (
    ClickStackTraceSourceMetadataMaterializedViews,
    ClickStackTraceSourceMetadataMaterializedViewsDict,
)
from .enums.use_text_index_for_implicit_column import UseTextIndexForImplicitColumnOrStr


class ClickStackTraceSource(SdkBaseModel):
    id: Optional[str] = UNSET
    """Unique source ID. Server-generated; ignored if sent in create/update requests."""

    name: str
    """Display name for the source."""

    section: Optional[str] = UNSET
    """Optional grouping label used to organize sources in the source selector. Sources that share a section value are
    displayed together."""

    disabled: OptionalNullable[bool] = UNSET
    """When true, the source is hidden from source selectors in the UI. Defaults to false."""

    kind: Literal["trace"] = "trace"
    """Source kind discriminator. Must be "trace" for trace sources."""

    connection: str
    """ID of the ClickHouse connection used by this source."""

    from_: ClickStackSourceFrom = Field(alias="from")
    query_settings: Optional[list[ClickStackQuerySetting]] = Field(default=UNSET, alias="querySettings")
    """Optional ClickHouse query settings applied when querying this source."""

    filter_settings: OptionalNullable[ClickStackSourceFilterSettings] = Field(default=UNSET, alias="filterSettings")
    default_table_select_expression: str = Field(alias="defaultTableSelectExpression")
    """Default columns selected in search results (this can be customized per search later)"""

    timestamp_value_expression: str = Field(alias="timestampValueExpression")
    """DateTime column or expression defines the start of the span"""

    duration_expression: str = Field(alias="durationExpression")
    """Expression to extract span duration."""

    duration_precision: int = Field(alias="durationPrecision")
    """Number of decimal digits in the duration value (e.g., 3 for milliseconds, 6 for microseconds, 9 for
    nanoseconds)."""

    trace_id_expression: str = Field(alias="traceIdExpression")
    """Expression to extract the trace ID."""

    span_id_expression: str = Field(alias="spanIdExpression")
    """Expression to extract the span ID."""

    parent_span_id_expression: str = Field(alias="parentSpanIdExpression")
    """Expression to extract the parent span ID."""

    span_name_expression: str = Field(alias="spanNameExpression")
    """Expression to extract the span name."""

    span_kind_expression: str = Field(alias="spanKindExpression")
    """Expression to extract the span kind (e.g., client, server, internal)."""

    log_source_id: OptionalNullable[str] = Field(default=UNSET, alias="logSourceId")
    """HyperDX Source for logs associated with traces. Optional"""

    session_source_id: OptionalNullable[str] = Field(default=UNSET, alias="sessionSourceId")
    """HyperDX Source for sessions associated with traces. Optional"""

    metric_source_id: OptionalNullable[str] = Field(default=UNSET, alias="metricSourceId")
    """HyperDX Source for metrics associated with traces. Optional"""

    status_code_expression: OptionalNullable[str] = Field(default=UNSET, alias="statusCodeExpression")
    """Expression to extract the span status code."""

    status_message_expression: OptionalNullable[str] = Field(default=UNSET, alias="statusMessageExpression")
    """Expression to extract the span status message."""

    service_name_expression: OptionalNullable[str] = Field(default=UNSET, alias="serviceNameExpression")
    """Expression to extract the service name from trace rows."""

    service_version_expression: OptionalNullable[str] = Field(default=UNSET, alias="serviceVersionExpression")
    """Expression identifying the running release of a service. Defaults to the OpenTelemetry service.version resource
    attribute when unset. Where services carry the release on different attributes, fall back across them with
    coalesce(nullIf(a, ''), nullIf(b, ''))."""

    resource_attributes_expression: OptionalNullable[str] = Field(default=UNSET, alias="resourceAttributesExpression")
    """Expression to extract resource-level attributes."""

    event_attributes_expression: OptionalNullable[str] = Field(default=UNSET, alias="eventAttributesExpression")
    """Expression to extract event-level attributes."""

    span_events_value_expression: OptionalNullable[str] = Field(default=UNSET, alias="spanEventsValueExpression")
    """Expression to extract span events. Used to capture events associated with spans. Expected to be Nested (
    Timestamp DateTime64(9), Name LowCardinality(String), Attributes Map(LowCardinality(String), String)"""

    implicit_column_expression: OptionalNullable[str] = Field(default=UNSET, alias="implicitColumnExpression")
    """Column used for full text search if no property is specified in a Lucene-based search. Typically the message body
    of a log."""

    known_columns_list_expression: OptionalNullable[str] = Field(default=UNSET, alias="knownColumnsListExpression")
    """For Distributed table sources whose target tables have non-matching column sets. A list of columns supported
    across all target tables, used instead of SELECT * when fetching full row data. Leave blank to select all
    columns."""

    use_text_index_for_implicit_column: OptionalNullable[UseTextIndexForImplicitColumnOrStr] = Field(
        default=UNSET, alias="useTextIndexForImplicitColumn"
    )
    """Controls whether lucene rendering uses ClickHouse text indices via hasAllTokens() against the implicit column.
    "auto" detects a covering index at query time, "enabled" forces text index usage, "disabled" forces a LIKE/hasToken
    fallback."""

    highlighted_trace_attribute_expressions: Optional[list[ClickStackHighlightedAttributeExpression]] = Field(
        default=UNSET, alias="highlightedTraceAttributeExpressions"
    )
    """Expressions defining trace-level attributes which are displayed in the trace view for the selected trace."""

    highlighted_row_attribute_expressions: Optional[list[ClickStackHighlightedAttributeExpression]] = Field(
        default=UNSET, alias="highlightedRowAttributeExpressions"
    )
    """Expressions defining row-level attributes which are displayed in the row side panel for the selected row"""

    materialized_views: Optional[list[ClickStackMaterializedView]] = Field(default=UNSET, alias="materializedViews")
    """Configure materialized views for query optimization. These pre-aggregated views can significantly improve query
    performance on aggregation queries."""

    metadata_materialized_views: OptionalNullable[ClickStackTraceSourceMetadataMaterializedViews] = Field(
        default=UNSET, alias="metadataMaterializedViews"
    )


class ClickStackTraceSourceDict(TypedDict):
    id: NotRequired[str]
    name: str
    section: NotRequired[str]
    disabled: NotRequired[bool | None]
    kind: Literal["trace"]
    connection: str
    from_: ClickStackSourceFromDict
    query_settings: NotRequired[list[ClickStackQuerySettingDict]]
    filter_settings: NotRequired[ClickStackSourceFilterSettingsDict | None]
    default_table_select_expression: str
    timestamp_value_expression: str
    duration_expression: str
    duration_precision: int
    trace_id_expression: str
    span_id_expression: str
    parent_span_id_expression: str
    span_name_expression: str
    span_kind_expression: str
    log_source_id: NotRequired[str | None]
    session_source_id: NotRequired[str | None]
    metric_source_id: NotRequired[str | None]
    status_code_expression: NotRequired[str | None]
    status_message_expression: NotRequired[str | None]
    service_name_expression: NotRequired[str | None]
    service_version_expression: NotRequired[str | None]
    resource_attributes_expression: NotRequired[str | None]
    event_attributes_expression: NotRequired[str | None]
    span_events_value_expression: NotRequired[str | None]
    implicit_column_expression: NotRequired[str | None]
    known_columns_list_expression: NotRequired[str | None]
    use_text_index_for_implicit_column: NotRequired[UseTextIndexForImplicitColumnOrStr | None]
    highlighted_trace_attribute_expressions: NotRequired[list[ClickStackHighlightedAttributeExpressionDict]]
    highlighted_row_attribute_expressions: NotRequired[list[ClickStackHighlightedAttributeExpressionDict]]
    materialized_views: NotRequired[list[ClickStackMaterializedViewDict]]
    metadata_materialized_views: NotRequired[ClickStackTraceSourceMetadataMaterializedViewsDict | None]
