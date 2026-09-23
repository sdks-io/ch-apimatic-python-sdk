from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.heatmap_scale_type import HeatmapScaleTypeOrStr


class ClickStackHeatmapSelectItem(SdkBaseModel):
    value_expression: str = Field(alias="valueExpression")
    """SQL expression for the value being bucketed on the y-axis. Must be non-empty."""

    count_expression: Optional[str] = Field(default=UNSET, alias="countExpression")
    """SQL expression for the count contributing to each bucket. Defaults to "count()" in the editor when omitted."""

    heatmap_scale_type: Optional[HeatmapScaleTypeOrStr] = Field(default=UNSET, alias="heatmapScaleType")
    """Scale type used to bucket values on the y-axis."""


class ClickStackHeatmapSelectItemDict(TypedDict):
    value_expression: str
    count_expression: NotRequired[str]
    heatmap_scale_type: NotRequired[HeatmapScaleTypeOrStr]
