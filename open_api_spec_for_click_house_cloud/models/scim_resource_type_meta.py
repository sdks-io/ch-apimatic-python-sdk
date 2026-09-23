from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScimResourceTypeMeta(SdkBaseModel):
    resource_type: str = Field(alias="resourceType")
    """The resource type."""

    location: str
    """The URI of this resource."""


class ScimResourceTypeMetaDict(TypedDict):
    resource_type: str
    location: str
