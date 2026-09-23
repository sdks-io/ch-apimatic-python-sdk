from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scim_schema import ScimSchema, ScimSchemaDict


class ScimSchemaListResponse(SdkBaseModel):
    schemas: list[str]
    """SCIM schema URIs."""

    total_results: int = Field(alias="totalResults")
    """Total number of schemas."""

    items_per_page: int = Field(alias="itemsPerPage")
    """Number of schemas per page."""

    start_index: int = Field(alias="startIndex")
    """1-based start index."""

    resources: list[ScimSchema] = Field(alias="Resources")
    """Array of schema definitions."""


class ScimSchemaListResponseDict(TypedDict):
    schemas: list[str]
    total_results: int
    items_per_page: int
    start_index: int
    resources: list[ScimSchemaDict]
