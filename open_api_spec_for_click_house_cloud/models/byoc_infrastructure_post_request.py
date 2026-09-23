from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.availability_zone_suffix import AvailabilityZoneSuffixOrStr
from .enums.region_id1 import RegionId1OrStr


class ByocInfrastructurePostRequest(SdkBaseModel):
    region_id: Optional[RegionId1OrStr] = Field(default=UNSET, alias="regionId")
    """Region in which the BYOC infrastructure will be located"""

    account_id: Optional[str] = Field(default=UNSET, alias="accountId")
    """Cloud account ID the BYOC infrastructure is configured for"""

    availability_zone_suffixes: Optional[list[AvailabilityZoneSuffixOrStr]] = Field(
        default=UNSET, alias="availabilityZoneSuffixes"
    )
    """List of availability zone suffixes"""

    vpc_cidr_range: Optional[str] = Field(default=UNSET, alias="vpcCidrRange")
    """CIDR range for VPC"""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Human readable name for infrastructure"""


class ByocInfrastructurePostRequestDict(TypedDict):
    region_id: NotRequired[RegionId1OrStr]
    account_id: NotRequired[str]
    availability_zone_suffixes: NotRequired[list[AvailabilityZoneSuffixOrStr]]
    vpc_cidr_range: NotRequired[str]
    display_name: NotRequired[str]
