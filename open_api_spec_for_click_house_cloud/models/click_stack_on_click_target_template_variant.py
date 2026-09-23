from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackOnClickTargetTemplateVariant(SdkBaseModel):
    mode: Literal["template"] = "template"
    """Target is matched by name against the template."""

    template: str
    """Name template rendered against the clicked row; supports ``{{column}}`` variables."""


class ClickStackOnClickTargetTemplateVariantDict(TypedDict):
    mode: Literal["template"]
    template: str
