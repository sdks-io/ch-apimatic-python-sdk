from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackDashboardContainerTab(SdkBaseModel):
    id: str
    """Unique identifier for the tab within its container."""

    title: str
    """Display title for the tab."""


class ClickStackDashboardContainerTabDict(TypedDict):
    id: str
    title: str
