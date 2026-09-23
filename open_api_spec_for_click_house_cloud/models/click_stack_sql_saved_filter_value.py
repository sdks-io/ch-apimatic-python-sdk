from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type18 import Type18OrStr


class ClickStackSqlSavedFilterValue(SdkBaseModel):
    type_: Optional[Type18OrStr] = Field(default=UNSET, alias="type")
    """Filter type."""

    condition: str
    """SQL filter condition. For example use expressions in the form "column IN ('value')"."""


class ClickStackSqlSavedFilterValueDict(TypedDict):
    type_: NotRequired[Type18OrStr]
    condition: str
