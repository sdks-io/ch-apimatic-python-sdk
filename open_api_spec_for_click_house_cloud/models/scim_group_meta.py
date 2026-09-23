from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ScimGroupMeta(SdkBaseModel):
    resource_type: str = Field(alias="resourceType")
    """Always "Group"."""

    created: RFC3339DateTime
    """DateTime the Group was created."""

    last_modified: RFC3339DateTime = Field(alias="lastModified")
    """DateTime the Group was last modified."""

    location: Optional[str] = UNSET
    """The URI of this Group resource."""


class ScimGroupMetaDict(TypedDict):
    resource_type: str
    created: RFC3339DateTime
    last_modified: RFC3339DateTime
    location: NotRequired[str]
