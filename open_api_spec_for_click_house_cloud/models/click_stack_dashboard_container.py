from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_dashboard_container_tab import ClickStackDashboardContainerTab, ClickStackDashboardContainerTabDict


class ClickStackDashboardContainer(SdkBaseModel):
    id: str
    """Unique identifier for the container within the dashboard."""

    title: str
    """Display title for the container."""

    collapsed: bool
    """Persisted default collapse state. Per-viewer state lives in the URL."""

    collapsible: Optional[bool] = UNSET
    """Whether the user can collapse the group."""

    bordered: Optional[bool] = UNSET
    """Whether to show a visual border around the group."""

    tabs: Optional[list[ClickStackDashboardContainerTab]] = UNSET
    """Optional tabs. 2+ entries renders a tab bar; 0-1 entries renders a plain group header. Tiles join a tab via
    tabId."""


class ClickStackDashboardContainerDict(TypedDict):
    id: str
    title: str
    collapsed: bool
    collapsible: NotRequired[bool]
    bordered: NotRequired[bool]
    tabs: NotRequired[list[ClickStackDashboardContainerTabDict]]
