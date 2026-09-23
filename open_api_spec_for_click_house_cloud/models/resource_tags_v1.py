from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ResourceTagsV1(SdkBaseModel):
    key: str
    """Tag key. Must be alphanumeric with dashes, underscores and dots."""

    value: Optional[str] = UNSET
    """Tag value. Must be alphanumeric with dashes, underscores and dots."""


class ResourceTagsV1Dict(TypedDict):
    key: str
    value: NotRequired[str]
