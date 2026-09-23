from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScimServiceProviderConfigMeta(SdkBaseModel):
    resource_type: str = Field(alias="resourceType")
    """The resource type of this resource."""

    location: str
    """The URI of this resource."""


class ScimServiceProviderConfigMetaDict(TypedDict):
    resource_type: str
    location: str
