from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scim_patch_operation import ScimPatchOperation, ScimPatchOperationDict


class ScimPatchOp(SdkBaseModel):
    schemas: list[str]
    """Must include "urn:ietf:params:scim:api:messages:2.0:PatchOp"."""

    operations: list[ScimPatchOperation] = Field(alias="Operations")
    """List of PATCH operations to apply."""


class ScimPatchOpDict(TypedDict):
    schemas: list[str]
    operations: list[ScimPatchOperationDict]
