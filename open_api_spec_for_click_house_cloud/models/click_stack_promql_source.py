from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_stack_query_setting import ClickStackQuerySetting, ClickStackQuerySettingDict
from .click_stack_source_from import ClickStackSourceFrom, ClickStackSourceFromDict


class ClickStackPromqlSource(SdkBaseModel):
    id: Optional[str] = UNSET
    """Unique source ID. Server-generated; ignored if sent in create/update requests."""

    name: str
    """Display name for the source."""

    section: Optional[str] = UNSET
    """Optional grouping label used to organize sources in the source selector. Sources that share a section value are
    displayed together."""

    disabled: OptionalNullable[bool] = UNSET
    """When true, the source is hidden from source selectors in the UI. Defaults to false."""

    kind: Literal["promql"] = "promql"
    """Source kind discriminator. Must be "promql" for PromQL sources."""

    connection: str
    """ID of the connection used by this source. Should reference a Prometheus-compatible connection."""

    from_: ClickStackSourceFrom = Field(alias="from")
    query_settings: Optional[list[ClickStackQuerySetting]] = Field(default=UNSET, alias="querySettings")
    """Optional ClickHouse query settings applied when querying this source."""

    timestamp_value_expression: str = Field(alias="timestampValueExpression")
    """Required by the API for all source kinds; not used when querying a Prometheus endpoint."""


class ClickStackPromqlSourceDict(TypedDict):
    id: NotRequired[str]
    name: str
    section: NotRequired[str]
    disabled: NotRequired[bool | None]
    kind: Literal["promql"]
    connection: str
    from_: ClickStackSourceFromDict
    query_settings: NotRequired[list[ClickStackQuerySettingDict]]
    timestamp_value_expression: str
