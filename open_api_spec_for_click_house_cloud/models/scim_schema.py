from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scim_schema_attribute import ScimSchemaAttribute, ScimSchemaAttributeDict
from .scim_schema_meta import ScimSchemaMeta, ScimSchemaMetaDict


class ScimSchema(SdkBaseModel):
    schemas: list[str]
    """SCIM schema URIs."""

    id: str
    """The unique URI of the schema."""

    name: str
    """The schema name."""

    description: str
    """A description of the schema."""

    attributes: list[ScimSchemaAttribute]
    """Service provider attributes comprising the schema."""

    meta: ScimSchemaMeta


class ScimSchemaDict(TypedDict):
    schemas: list[str]
    id: str
    name: str
    description: str
    attributes: list[ScimSchemaAttributeDict]
    meta: ScimSchemaMetaDict
