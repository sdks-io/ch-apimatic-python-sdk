from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.click_stack_dashboard_chart_series import (
    ClickStackDashboardChartSeries,
    ClickStackDashboardChartSeriesDict,
)
from .unions.click_stack_tile_config import ClickStackTileConfig, ClickStackTileConfigDict


class ClickStackTileInput(SdkBaseModel):
    name: str
    """Display name for the tile"""

    x: int
    """Horizontal position in the grid (0-based)"""

    y: int
    """Vertical position in the grid (0-based)"""

    w: int
    """Width in grid units"""

    h: int
    """Height in grid units"""

    config: Optional[ClickStackTileConfig] = UNSET
    container_id: Optional[str] = Field(default=UNSET, alias="containerId")
    """References a DashboardContainer by id. Tiles without containerId render in the default ungrouped area."""

    tab_id: Optional[str] = Field(default=UNSET, alias="tabId")
    """References a tab inside the tile's container by id. Requires containerId to be set, and the container to declare
    a matching tab."""

    id: Optional[str] = UNSET
    """Optional tile ID. Omit to generate a new ID."""

    as_ratio: Optional[bool] = Field(default=UNSET, alias="asRatio")
    """Display two series as a ratio (series[0] / series[1]). Only applicable when providing "series". Deprecated in
    favor of "config.asRatio"."""

    series: Optional[list[ClickStackDashboardChartSeries]] = UNSET
    """Data series to display in this tile (all must be the same type). Deprecated; use "config" instead."""


class ClickStackTileInputDict(TypedDict):
    name: str
    x: int
    y: int
    w: int
    h: int
    config: NotRequired[ClickStackTileConfigDict]
    container_id: NotRequired[str]
    tab_id: NotRequired[str]
    id: NotRequired[str]
    as_ratio: NotRequired[bool]
    series: NotRequired[list[ClickStackDashboardChartSeriesDict]]
