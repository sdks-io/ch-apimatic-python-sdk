from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scim_schema_sub_attribute import ScimSchemaSubAttribute, ScimSchemaSubAttributeDict


class ScimSchemaAttribute(SdkBaseModel):
    name: str
    """The attribute name."""

    type_: str = Field(alias="type")
    """The attribute type (e.g., "string", "boolean", "complex")."""

    sub_attributes: Optional[list[ScimSchemaSubAttribute]] = Field(default=UNSET, alias="subAttributes")
    """Sub-attributes for complex attributes."""

    multi_valued: bool = Field(alias="multiValued")
    """Whether the attribute can have multiple values."""

    description: str
    """A human-readable description of the attribute."""

    required: bool
    """Whether the attribute is required."""

    case_exact: Optional[bool] = Field(default=UNSET, alias="caseExact")
    """Whether the string attribute is case sensitive."""

    mutability: str
    """The circumstances under which the value of the attribute can be (re)defined."""

    returned: str
    """The circumstances under which an attribute and associated values are returned."""

    uniqueness: Optional[str] = UNSET
    """How the service provider enforces uniqueness of attribute values."""

    reference_types: Optional[list[str]] = Field(default=UNSET, alias="referenceTypes")
    """A multi-valued array of JSON strings."""

    canonical_values: Optional[list[str]] = Field(default=UNSET, alias="canonicalValues")
    """A collection of suggested canonical values that MAY be used."""


class ScimSchemaAttributeDict(TypedDict):
    name: str
    type_: str
    sub_attributes: NotRequired[list[ScimSchemaSubAttributeDict]]
    multi_valued: bool
    description: str
    required: bool
    case_exact: NotRequired[bool]
    mutability: str
    returned: str
    uniqueness: NotRequired[str]
    reference_types: NotRequired[list[str]]
    canonical_values: NotRequired[list[str]]
