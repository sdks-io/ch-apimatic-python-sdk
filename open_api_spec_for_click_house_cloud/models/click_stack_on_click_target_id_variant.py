from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackOnClickTargetIdVariant(SdkBaseModel):
    mode: Literal["id"] = "id"
    """Target is a single dashboard or log/trace source"""

    id: str
    """ID of the target source (for search) or dashboard (for dashboard)."""


class ClickStackOnClickTargetIdVariantDict(TypedDict):
    mode: Literal["id"]
    id: str
