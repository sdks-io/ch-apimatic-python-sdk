from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_saved_search_filter import ClickStackSavedSearchFilter, ClickStackSavedSearchFilterDict
from .enums.where_language12 import WhereLanguage12OrStr


class ClickStackSavedSearchInput(SdkBaseModel):
    name: str
    """Display name for the saved search."""

    source_id: str = Field(alias="sourceId")
    """ID of the source to query. Must belong to the team."""

    select: Optional[str] = UNSET
    """Comma-separated list of column expressions to display. Empty uses the source default."""

    where: Optional[str] = UNSET
    """Row filter expression. The language is controlled by whereLanguage."""

    where_language: Optional[WhereLanguage12OrStr] = Field(default=UNSET, alias="whereLanguage")
    """Language used for the where filter."""

    order_by: Optional[str] = Field(default=UNSET, alias="orderBy")
    """ORDER BY expression. Empty uses the source default."""

    tags: Optional[list[str]] = UNSET
    """Tags used to organize saved searches."""

    filters: Optional[list[ClickStackSavedSearchFilter]] = UNSET
    """Structured pinned filters applied to the search."""


class ClickStackSavedSearchInputDict(TypedDict):
    name: str
    source_id: str
    select: NotRequired[str]
    where: NotRequired[str]
    where_language: NotRequired[WhereLanguage12OrStr]
    order_by: NotRequired[str]
    tags: NotRequired[list[str]]
    filters: NotRequired[list[ClickStackSavedSearchFilterDict]]
