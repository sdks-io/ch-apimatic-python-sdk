from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .click_stack_validate_dashboard_error import ClickStackValidateDashboardError, ClickStackValidateDashboardErrorDict


class ClickStackValidateDashboardResponse(SdkBaseModel):
    valid: bool
    """True when the body passes all validation rules."""

    errors: list[ClickStackValidateDashboardError]
    """Validation errors. Empty when valid is true."""

    normalized: Any | None


class ClickStackValidateDashboardResponseDict(TypedDict):
    valid: bool
    errors: list[ClickStackValidateDashboardErrorDict]
    normalized: Any | None
