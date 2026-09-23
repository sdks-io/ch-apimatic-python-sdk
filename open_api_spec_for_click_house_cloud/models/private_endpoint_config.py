from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrivateEndpointConfig(SdkBaseModel):
    endpoint_service_id: Optional[str] = Field(default=UNSET, alias="endpointServiceId")
    """Unique identifier of the interface endpoint you created in your VPC with the AWS(Service Name), GCP(Target
    Service) or AZURE (Private Link Service) resource"""

    private_dns_hostname: Optional[str] = Field(default=UNSET, alias="privateDnsHostname")
    """Private DNS Hostname of the VPC you created"""


class PrivateEndpointConfigDict(TypedDict):
    endpoint_service_id: NotRequired[str]
    private_dns_hostname: NotRequired[str]
