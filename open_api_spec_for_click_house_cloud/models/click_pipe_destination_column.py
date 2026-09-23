from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickPipeDestinationColumn(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the column."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Type of the column."""


class ClickPipeDestinationColumnDict(TypedDict):
    name: NotRequired[str]
    type_: NotRequired[str]
