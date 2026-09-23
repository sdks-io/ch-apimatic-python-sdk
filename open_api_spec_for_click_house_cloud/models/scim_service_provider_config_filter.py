from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScimServiceProviderConfigFilter(SdkBaseModel):
    supported: bool
    """Whether filter is supported."""

    max_results: int = Field(alias="maxResults")
    """Maximum number of results per filter query."""


class ScimServiceProviderConfigFilterDict(TypedDict):
    supported: bool
    max_results: int
