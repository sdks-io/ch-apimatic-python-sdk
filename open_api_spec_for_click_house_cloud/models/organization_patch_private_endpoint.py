from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cloud_provider1 import CloudProvider1OrStr
from .enums.region1 import Region1OrStr


class OrganizationPatchPrivateEndpoint(SdkBaseModel):
    id: Optional[str] = UNSET
    """Private endpoint identifier"""

    description: Optional[str] = UNSET
    """Optional description of private endpoint"""

    cloud_provider: Optional[CloudProvider1OrStr] = Field(default=UNSET, alias="cloudProvider")
    """Cloud provider in which the private endpoint is lcoated"""

    region: Optional[Region1OrStr] = UNSET
    """Region in which the private endpoint is located"""


class OrganizationPatchPrivateEndpointDict(TypedDict):
    id: NotRequired[str]
    description: NotRequired[str]
    cloud_provider: NotRequired[CloudProvider1OrStr]
    region: NotRequired[Region1OrStr]
