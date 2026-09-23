from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_stack_dashboard_container import ClickStackDashboardContainer, ClickStackDashboardContainerDict
from .click_stack_filter import ClickStackFilter, ClickStackFilterDict
from .click_stack_tile_output import ClickStackTileOutput, ClickStackTileOutputDict
from .enums.saved_query_language import SavedQueryLanguageOrStr
from .unions.click_stack_saved_filter_value import ClickStackSavedFilterValue, ClickStackSavedFilterValueDict


class ClickStackDashboardResponse(SdkBaseModel):
    id: Optional[str] = UNSET
    """Dashboard ID"""

    name: Optional[str] = UNSET
    """Dashboard name"""

    tiles: Optional[list[ClickStackTileOutput]] = UNSET
    """List of tiles/charts in the dashboard"""

    tags: Optional[list[str]] = UNSET
    """Tags for organizing and filtering dashboards"""

    filters: Optional[list[ClickStackFilter]] = UNSET
    """Dropdown filters added to the dashboard. Each one broadcasts its selected value as a condition, acts as a
    variable which can be referenced in tile queries, or both."""

    saved_query: OptionalNullable[str] = Field(default=UNSET, alias="savedQuery")
    """Optional default dashboard query restored when loading the dashboard."""

    saved_query_language: OptionalNullable[SavedQueryLanguageOrStr] = Field(default=UNSET, alias="savedQueryLanguage")
    """Query language used by savedQuery."""

    saved_filter_values: Optional[list[ClickStackSavedFilterValue]] = Field(default=UNSET, alias="savedFilterValues")
    """Optional default dashboard filter values restored when loading the dashboard."""

    containers: Optional[list[ClickStackDashboardContainer]] = UNSET
    """Optional grouping containers. Each tile may join a container via tile.containerId, and a tab inside it via
    tile.tabId."""


class ClickStackDashboardResponseDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    tiles: NotRequired[list[ClickStackTileOutputDict]]
    tags: NotRequired[list[str]]
    filters: NotRequired[list[ClickStackFilterDict]]
    saved_query: NotRequired[str | None]
    saved_query_language: NotRequired[SavedQueryLanguageOrStr | None]
    saved_filter_values: NotRequired[list[ClickStackSavedFilterValueDict]]
    containers: NotRequired[list[ClickStackDashboardContainerDict]]
