from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.where_language4 import WhereLanguage4OrStr


class ClickStackSearchChartConfig(SdkBaseModel):
    display_type: Literal["search"] = Field(default="search", alias="displayType")
    """Display type discriminator. Must be "search" for search/log viewer tiles."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query."""

    select: str
    """Comma-separated list of expressions to display."""

    where: Optional[str] = UNSET
    """Filter condition for the search (syntax depends on whereLanguage)."""

    where_language: WhereLanguage4OrStr = Field(alias="whereLanguage")
    """Query language for the where clause."""


class ClickStackSearchChartConfigDict(TypedDict):
    display_type: Literal["search"]
    source_id: str
    select: str
    where: NotRequired[str]
    where_language: WhereLanguage4OrStr
