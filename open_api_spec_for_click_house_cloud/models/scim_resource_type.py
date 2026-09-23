from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scim_resource_type_meta import ScimResourceTypeMeta, ScimResourceTypeMetaDict
from .scim_schema_extension import ScimSchemaExtension, ScimSchemaExtensionDict


class ScimResourceType(SdkBaseModel):
    schemas: list[str]
    """SCIM schema URIs."""

    id: str
    """The resource type ID."""

    name: str
    """The resource type name."""

    endpoint: str
    """The endpoint path for this resource type."""

    description: str
    """A description of the resource type."""

    schema_value: str = Field(alias="schema")
    """The primary schema URI for this resource type."""

    schema_extensions: list[ScimSchemaExtension] = Field(alias="schemaExtensions")
    """Optional schema extensions for this resource type."""

    meta: ScimResourceTypeMeta


class ScimResourceTypeDict(TypedDict):
    schemas: list[str]
    id: str
    name: str
    endpoint: str
    description: str
    schema_value: str
    schema_extensions: list[ScimSchemaExtensionDict]
    meta: ScimResourceTypeMetaDict
