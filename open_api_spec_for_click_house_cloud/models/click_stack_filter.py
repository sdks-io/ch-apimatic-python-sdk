from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.source_metric_type import SourceMetricTypeOrStr
from .enums.where_language10 import WhereLanguage10OrStr


class ClickStackFilter(SdkBaseModel):
    type_: Literal["QUERY_EXPRESSION"] = Field(default="QUERY_EXPRESSION", alias="type")
    """Filter type. Must be "QUERY_EXPRESSION"."""

    name: str
    """Display name for the dashboard filter key"""

    expression: str
    """SQL expression used when querying values for this filter, and when applying this dashboard filter to tiles."""

    source_id: str = Field(alias="sourceId")
    """Source ID this dashboard filter key applies to"""

    source_metric_type: Optional[SourceMetricTypeOrStr] = Field(default=UNSET, alias="sourceMetricType")
    """Metric type when source is metrics"""

    where: Optional[str] = UNSET
    """Optional WHERE condition to scope which rows this filter key reads values from"""

    where_language: Optional[WhereLanguage10OrStr] = Field(default=UNSET, alias="whereLanguage")
    """Language of the where condition"""

    applies_to_source_ids: Optional[list[str]] = Field(default=UNSET, alias="appliesToSourceIds")
    """Optional list of source IDs this filter applies to. Omit or provide an empty array to apply the filter to ALL
    tiles regardless of source. A non-empty array restricts the filter to only tiles whose source ID is in the list;
    tiles using other sources are not affected by the selected filter value(s). Scopes the broadcast condition only, so
    a non-empty array is rejected when isBroadcastEnabled is false, and is omitted from responses for such a filter."""

    is_broadcast_enabled: Optional[bool] = Field(default=UNSET, alias="isBroadcastEnabled")
    """Whether the selected value is applied as a filter condition on every builder tile this filter applies to (see
    appliesToSourceIds), and every raw sql tile using the $__filters macro. Omitting the field means enabled."""

    is_variable_enabled: Optional[bool] = Field(default=UNSET, alias="isVariableEnabled")
    """Whether the selected value is exposed to tile queries as a dashboard variable named by variableName. Tiles may
    reference it as ``$variableName`` or using the (preferred) ``$__filter($<variableName>)`` and
    ``$__conditionalAll(<condition>, $<variableName>)`` macros."""

    variable_name: Optional[str] = Field(default=UNSET, alias="variableName")
    """Token tiles reference this filter's selected value by, as ``$variableName``. Must start with a letter and may
    contain only letters, numbers, and underscores. Defaults to the display name with whitespace replaced by underscores
    and remaining illegal characters removed, so a variable-enabled filter whose name derives nothing usable must send
    this field explicitly. Variable names must be unique across a dashboard's variable-enabled filters. Names the
    variable only, so the field is rejected when isVariableEnabled is not true, and is omitted from responses for such a
    filter."""

    id: str
    """Unique dashboard filter key ID"""


class ClickStackFilterDict(TypedDict):
    type_: Literal["QUERY_EXPRESSION"]
    name: str
    expression: str
    source_id: str
    source_metric_type: NotRequired[SourceMetricTypeOrStr]
    where: NotRequired[str]
    where_language: NotRequired[WhereLanguage10OrStr]
    applies_to_source_ids: NotRequired[list[str]]
    is_broadcast_enabled: NotRequired[bool]
    is_variable_enabled: NotRequired[bool]
    variable_name: NotRequired[str]
    id: str
