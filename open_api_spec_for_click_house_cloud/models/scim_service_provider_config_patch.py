from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScimServiceProviderConfigPatch(SdkBaseModel):
    supported: bool
    """Whether PATCH is supported."""


class ScimServiceProviderConfigPatchDict(TypedDict):
    supported: bool
