from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scim_group import ScimGroup, ScimGroupDict


class ScimGroupListResponse(SdkBaseModel):
    schemas: list[str]
    """Must be ["urn:ietf:params:scim:api:messages:2.0:ListResponse"]."""

    total_results: int = Field(alias="totalResults")
    """Total number of Groups matching the query."""

    start_index: int = Field(alias="startIndex")
    """1-based index of the first result in the current set."""

    items_per_page: int = Field(alias="itemsPerPage")
    """Number of resources returned in this response."""

    resources: list[ScimGroup] = Field(alias="Resources")
    """Array of SCIM Group resources."""


class ScimGroupListResponseDict(TypedDict):
    schemas: list[str]
    total_results: int
    start_index: int
    items_per_page: int
    resources: list[ScimGroupDict]
