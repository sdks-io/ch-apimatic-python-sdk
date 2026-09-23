from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ScimUserMeta(SdkBaseModel):
    resource_type: str = Field(alias="resourceType")
    """The name of the resource type of the resource."""

    created: RFC3339DateTime
    """The DateTime the Resource was added to the Service Provider."""

    last_modified: RFC3339DateTime = Field(alias="lastModified")
    """The most recent DateTime the details of this Resource were updated."""

    location: Optional[str] = UNSET
    """The URI of the resource being returned."""


class ScimUserMetaDict(TypedDict):
    resource_type: str
    created: RFC3339DateTime
    last_modified: RFC3339DateTime
    location: NotRequired[str]
