from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.click_stack_tile_config import ClickStackTileConfig, ClickStackTileConfigDict


class ClickStackTileOutput(SdkBaseModel):
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

    id: str
    """Unique tile ID assigned by the server."""


class ClickStackTileOutputDict(TypedDict):
    name: str
    x: int
    y: int
    w: int
    h: int
    config: NotRequired[ClickStackTileConfigDict]
    container_id: NotRequired[str]
    tab_id: NotRequired[str]
    id: str
