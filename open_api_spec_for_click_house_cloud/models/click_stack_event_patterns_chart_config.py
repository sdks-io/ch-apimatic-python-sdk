from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.where_language4 import WhereLanguage4OrStr


class ClickStackEventPatternsChartConfig(SdkBaseModel):
    display_type: Literal["event_patterns"] = Field(default="event_patterns", alias="displayType")
    """Display type discriminator. Must be "event_patterns" for pattern mining tiles."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to mine patterns from."""

    select: Optional[str] = UNSET
    """Column or expression to mine patterns from. Leave empty to use the source default (Body for logs, SpanName for
    traces)."""

    where: Optional[str] = UNSET
    """Filter condition for the pattern mining query (syntax depends on whereLanguage)."""

    where_language: Optional[WhereLanguage4OrStr] = Field(default=UNSET, alias="whereLanguage")
    """Query language for the where clause."""


class ClickStackEventPatternsChartConfigDict(TypedDict):
    display_type: Literal["event_patterns"]
    source_id: str
    select: NotRequired[str]
    where: NotRequired[str]
    where_language: NotRequired[WhereLanguage4OrStr]
