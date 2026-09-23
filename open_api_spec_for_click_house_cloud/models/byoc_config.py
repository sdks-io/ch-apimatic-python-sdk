from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cloud_provider2 import CloudProvider2OrStr
from .enums.region_id import RegionIdOrStr
from .enums.state1 import State1OrStr


class ByocConfig(SdkBaseModel):
    id: Optional[str] = UNSET
    """Unique identifier of the BYOC configuration"""

    state: Optional[State1OrStr] = UNSET
    """State of the infrastructure"""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Name of the account"""

    region_id: Optional[RegionIdOrStr] = Field(default=UNSET, alias="regionId")
    """Region for which the BYOC has been configured and where it is possible to create services"""

    cloud_provider: Optional[CloudProvider2OrStr] = Field(default=UNSET, alias="cloudProvider")
    """Cloud provider of the region"""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Human readable name for infrastructure"""


class ByocConfigDict(TypedDict):
    id: NotRequired[str]
    state: NotRequired[State1OrStr]
    account_name: NotRequired[str]
    region_id: NotRequired[RegionIdOrStr]
    cloud_provider: NotRequired[CloudProvider2OrStr]
    display_name: NotRequired[str]
