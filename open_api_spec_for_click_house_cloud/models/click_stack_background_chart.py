from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.color import ColorOrStr
from .enums.type19 import Type19OrStr


class ClickStackBackgroundChart(SdkBaseModel):
    type_: Type19OrStr = Field(alias="type")
    """Sparkline shape."""

    color: Optional[ColorOrStr] = UNSET
    """Optional palette-token override for the sparkline. When unset the sparkline inherits the tile's static color."""


class ClickStackBackgroundChartDict(TypedDict):
    type_: Type19OrStr
    color: NotRequired[ColorOrStr]
