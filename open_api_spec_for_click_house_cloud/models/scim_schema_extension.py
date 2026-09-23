from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScimSchemaExtension(SdkBaseModel):
    schema_value: str = Field(alias="schema")
    """The URI of a schema extension."""

    required: bool
    """Whether the schema extension is required."""


class ScimSchemaExtensionDict(TypedDict):
    schema_value: str
    required: bool
