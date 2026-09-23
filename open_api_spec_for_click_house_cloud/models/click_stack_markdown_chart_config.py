from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickStackMarkdownChartConfig(SdkBaseModel):
    display_type: Literal["markdown"] = Field(default="markdown", alias="displayType")
    """Display type discriminator. Must be "markdown" for markdown text tiles."""

    markdown: Optional[str] = UNSET
    """Markdown content to render inside the tile."""


class ClickStackMarkdownChartConfigDict(TypedDict):
    display_type: Literal["markdown"]
    markdown: NotRequired[str]
