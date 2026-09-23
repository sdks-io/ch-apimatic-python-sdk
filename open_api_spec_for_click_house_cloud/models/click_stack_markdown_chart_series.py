from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackMarkdownChartSeries(SdkBaseModel):
    type_: Literal["markdown"] = Field(default="markdown", alias="type")
    """Series type discriminator. Must be "markdown" for markdown text widgets."""

    content: str
    """Markdown content to render inside the widget."""


class ClickStackMarkdownChartSeriesDict(TypedDict):
    type_: Literal["markdown"]
    content: str
