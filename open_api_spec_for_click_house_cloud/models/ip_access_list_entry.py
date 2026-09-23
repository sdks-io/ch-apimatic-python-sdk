from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IpAccessListEntry(SdkBaseModel):
    source: Optional[str] = UNSET
    """IP or CIDR"""

    description: Optional[str] = UNSET
    """Optional description of IPv4 address or IPv4 CIDR to allow access from"""


class IpAccessListEntryDict(TypedDict):
    source: NotRequired[str]
    description: NotRequired[str]
