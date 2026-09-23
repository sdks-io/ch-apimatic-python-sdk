from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackValidateDashboardError(SdkBaseModel):
    path: str
    """Dot-separated field path, or empty string for top-level errors."""

    message: str
    """Human-readable error description."""


class ClickStackValidateDashboardErrorDict(TypedDict):
    path: str
    message: str
