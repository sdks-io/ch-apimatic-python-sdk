from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomPrivateDnsMapping(SdkBaseModel):
    private_dns_name: Optional[str] = Field(default=UNSET, alias="privateDnsName")
    """Optional private DNS names for Reverse Private Endpoint. Can be used as data source destination address. Must be
    unique across the ClickHouse service. Generally available for Google Private Service Connect (PSC). For AWS
    PrivateLink (VPC endpoint service and VPC resource), available in Private Preview; contact ClickHouse support to
    enable it for your service. Not supported for MSK multi-VPC. Supports exact names and leading wildcard names such as
    *.example.com"""


class CustomPrivateDnsMappingDict(TypedDict):
    private_dns_name: NotRequired[str]
