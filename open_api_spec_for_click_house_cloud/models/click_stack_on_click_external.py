from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackOnClickExternal(SdkBaseModel):
    type_: Literal["external"] = Field(default="external", alias="type")
    """OnClick variant discriminator. Must be "external" for external link-outs."""

    url_template: str = Field(alias="urlTemplate")
    """Handlebars template rendered against the clicked row; supports ``{{column}}`` variables. The rendered value must
    be an absolute http(s) URL."""


class ClickStackOnClickExternalDict(TypedDict):
    type_: Literal["external"]
    url_template: str
