from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .organization_patch_private_endpoint import OrganizationPatchPrivateEndpoint, OrganizationPatchPrivateEndpointDict


class OrganizationPrivateEndpointsPatch(SdkBaseModel):
    add: Optional[list[OrganizationPatchPrivateEndpoint]] = UNSET
    """DEPRECATED. Elements to add. Executed after "remove" part is processed. Please use the ``Update Service Basic
    Details`` endpoint with the ``privateEndpointIds`` field instead to modify the private endpoints."""

    remove: Optional[list[OrganizationPatchPrivateEndpoint]] = UNSET
    """Elements to remove. Executed before "add" part is processed."""


class OrganizationPrivateEndpointsPatchDict(TypedDict):
    add: NotRequired[list[OrganizationPatchPrivateEndpointDict]]
    remove: NotRequired[list[OrganizationPatchPrivateEndpointDict]]
