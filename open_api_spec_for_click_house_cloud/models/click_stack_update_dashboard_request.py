from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_stack_dashboard_container import ClickStackDashboardContainer, ClickStackDashboardContainerDict
from .click_stack_filter import ClickStackFilter, ClickStackFilterDict
from .click_stack_tile_input import ClickStackTileInput, ClickStackTileInputDict
from .enums.saved_query_language import SavedQueryLanguageOrStr
from .unions.click_stack_saved_filter_value import ClickStackSavedFilterValue, ClickStackSavedFilterValueDict


class ClickStackUpdateDashboardRequest(SdkBaseModel):
    name: str
    """Dashboard name."""

    tiles: list[ClickStackTileInput]
    """Full list of tiles for the dashboard. Existing tiles are matched by ID; tiles with an ID that does not match an
    existing tile will be assigned a new generated ID."""

    tags: Optional[list[str]] = UNSET
    """Tags for organizing and filtering dashboards."""

    filters: Optional[list[ClickStackFilter]] = UNSET
    """Dropdown filters added to the dashboard. Each one broadcasts its selected value as a condition, acts as a
    variable which can be referenced in tile queries, or both."""

    saved_query: OptionalNullable[str] = Field(default=UNSET, alias="savedQuery")
    """Optional default dashboard query to persist on the dashboard."""

    saved_query_language: OptionalNullable[SavedQueryLanguageOrStr] = Field(default=UNSET, alias="savedQueryLanguage")
    """Query language used by savedQuery."""

    saved_filter_values: Optional[list[ClickStackSavedFilterValue]] = Field(default=UNSET, alias="savedFilterValues")
    """Optional default dashboard filter values to persist on the dashboard."""

    containers: Optional[list[ClickStackDashboardContainer]] = UNSET
    """Optional grouping containers. Each tile may join a container via tile.containerId, and a tab inside it via
    tile.tabId."""


class ClickStackUpdateDashboardRequestDict(TypedDict):
    name: str
    tiles: list[ClickStackTileInputDict]
    tags: NotRequired[list[str]]
    filters: NotRequired[list[ClickStackFilterDict]]
    saved_query: NotRequired[str | None]
    saved_query_language: NotRequired[SavedQueryLanguageOrStr | None]
    saved_filter_values: NotRequired[list[ClickStackSavedFilterValueDict]]
    containers: NotRequired[list[ClickStackDashboardContainerDict]]
