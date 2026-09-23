from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scim_resource_type import ScimResourceType, ScimResourceTypeDict


class ScimResourceTypeListResponse(SdkBaseModel):
    schemas: list[str]
    """SCIM schema URIs."""

    total_results: int = Field(alias="totalResults")
    """Total number of resource types."""

    items_per_page: int = Field(alias="itemsPerPage")
    """Number of resources per page."""

    start_index: int = Field(alias="startIndex")
    """1-based start index."""

    resources: list[ScimResourceType] = Field(alias="Resources")
    """Array of resource type definitions."""


class ScimResourceTypeListResponseDict(TypedDict):
    schemas: list[str]
    total_results: int
    items_per_page: int
    start_index: int
    resources: list[ScimResourceTypeDict]
