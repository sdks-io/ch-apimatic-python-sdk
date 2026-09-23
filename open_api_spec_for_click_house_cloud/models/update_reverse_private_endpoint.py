from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_private_dns_mapping import CustomPrivateDnsMapping, CustomPrivateDnsMappingDict


class UpdateReversePrivateEndpoint(SdkBaseModel):
    custom_private_dns_mappings: Optional[list[CustomPrivateDnsMapping]] = Field(
        default=UNSET, alias="customPrivateDnsMappings"
    )
    """Optional private DNS names for Reverse Private Endpoint. Can be used as data source destination address. Must be
    unique across the ClickHouse service. Generally available for Google Private Service Connect (PSC). For AWS
    PrivateLink (VPC endpoint service and VPC resource), available in Private Preview; contact ClickHouse support to
    enable it for your service. Not supported for MSK multi-VPC. Supports exact names and leading wildcard names such as
    *.example.com"""


class UpdateReversePrivateEndpointDict(TypedDict):
    custom_private_dns_mappings: NotRequired[list[CustomPrivateDnsMappingDict]]
