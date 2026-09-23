from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.where_language import WhereLanguageOrStr


class ClickStackSearchChartSeries(SdkBaseModel):
    type_: Literal["search"] = Field(default="search", alias="type")
    """Series type discriminator. Must be "search" for search/log viewer charts."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query"""

    fields: list[str]
    """List of field names to display in the search results table"""

    where: str
    """Filter query for the data (syntax depends on whereLanguage)"""

    where_language: WhereLanguageOrStr = Field(alias="whereLanguage")
    """Query language for the where clause"""


class ClickStackSearchChartSeriesDict(TypedDict):
    type_: Literal["search"]
    source_id: str
    fields: list[str]
    where: str
    where_language: WhereLanguageOrStr
