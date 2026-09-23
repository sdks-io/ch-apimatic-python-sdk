from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScimBooleanFeature(SdkBaseModel):
    supported: bool
    """Whether the feature is supported."""


class ScimBooleanFeatureDict(TypedDict):
    supported: bool
