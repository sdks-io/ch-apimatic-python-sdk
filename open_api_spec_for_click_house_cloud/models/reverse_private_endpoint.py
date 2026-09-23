from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_private_dns_mapping import CustomPrivateDnsMapping, CustomPrivateDnsMappingDict
from .enums.msk_authentication import MskAuthenticationOrStr
from .enums.status import StatusOrStr
from .enums.type1 import Type1OrStr


class ReversePrivateEndpoint(SdkBaseModel):
    description: Optional[str] = UNSET
    """Reverse private endpoint description. Maximum length is 255 characters."""

    type_: Optional[Type1OrStr] = Field(default=UNSET, alias="type")
    """Reverse private endpoint type."""

    vpc_endpoint_service_name: OptionalNullable[str] = Field(default=UNSET, alias="vpcEndpointServiceName")
    """VPC endpoint service name."""

    vpc_resource_configuration_id: OptionalNullable[str] = Field(default=UNSET, alias="vpcResourceConfigurationId")
    """VPC resource configuration ID. Required for VPC_RESOURCE type."""

    vpc_resource_share_arn: OptionalNullable[str] = Field(default=UNSET, alias="vpcResourceShareArn")
    """VPC resource share ARN. Required for VPC_RESOURCE type."""

    msk_cluster_arn: OptionalNullable[str] = Field(default=UNSET, alias="mskClusterArn")
    """MSK cluster ARN. Required for MSK_MULTI_VPC type."""

    msk_authentication: OptionalNullable[MskAuthenticationOrStr] = Field(default=UNSET, alias="mskAuthentication")
    """MSK cluster authentication type. Required for MSK_MULTI_VPC type."""

    gcp_service_attachment: OptionalNullable[str] = Field(default=UNSET, alias="gcpServiceAttachment")
    """Private Preview. GCP PSC service attachment URI. Required for GCP_PSC_SERVICE_ATTACHMENT type. Format:
    projects/{project}/regions/{region}/serviceAttachments/{name}."""

    custom_private_dns_mappings: Optional[list[CustomPrivateDnsMapping]] = Field(
        default=UNSET, alias="customPrivateDnsMappings"
    )
    """Optional private DNS names for Reverse Private Endpoint. Can be used as data source destination address. Must be
    unique across the ClickHouse service. Generally available for Google Private Service Connect (PSC). For AWS
    PrivateLink (VPC endpoint service and VPC resource), available in Private Preview; contact ClickHouse support to
    enable it for your service. Not supported for MSK multi-VPC. Supports exact names and leading wildcard names such as
    *.example.com"""

    id: Optional[UUID] = UNSET
    """Reverse private endpoint ID."""

    service_id: Optional[UUID] = Field(default=UNSET, alias="serviceId")
    """ClickHouse service ID reverse private endpoint is associated with."""

    endpoint_id: Optional[str] = Field(default=UNSET, alias="endpointId")
    """Reverse private endpoint endpoint ID."""

    dns_names: Optional[list[str]] = Field(default=UNSET, alias="dnsNames")
    """Reverse private endpoint internal DNS names."""

    private_dns_names: Optional[list[str]] = Field(default=UNSET, alias="privateDnsNames")
    """Reverse private endpoint private DNS names."""

    status: Optional[StatusOrStr] = UNSET
    """Reverse private endpoint status."""


class ReversePrivateEndpointDict(TypedDict):
    description: NotRequired[str]
    type_: NotRequired[Type1OrStr]
    vpc_endpoint_service_name: NotRequired[str | None]
    vpc_resource_configuration_id: NotRequired[str | None]
    vpc_resource_share_arn: NotRequired[str | None]
    msk_cluster_arn: NotRequired[str | None]
    msk_authentication: NotRequired[MskAuthenticationOrStr | None]
    gcp_service_attachment: NotRequired[str | None]
    custom_private_dns_mappings: NotRequired[list[CustomPrivateDnsMappingDict]]
    id: NotRequired[UUID]
    service_id: NotRequired[UUID]
    endpoint_id: NotRequired[str]
    dns_names: NotRequired[list[str]]
    private_dns_names: NotRequired[list[str]]
    status: NotRequired[StatusOrStr]
