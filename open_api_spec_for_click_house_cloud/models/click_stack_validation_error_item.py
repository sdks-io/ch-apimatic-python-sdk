from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickStackValidationErrorItem(SdkBaseModel):
    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Request part that failed validation."""

    errors: Optional[Any] = UNSET


class ClickStackValidationErrorItemDict(TypedDict):
    type_: NotRequired[str]
    errors: NotRequired[Any]
