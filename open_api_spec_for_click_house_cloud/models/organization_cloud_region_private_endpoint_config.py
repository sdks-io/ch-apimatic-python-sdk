from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OrganizationCloudRegionPrivateEndpointConfig(SdkBaseModel):
    endpoint_service_id: Optional[str] = Field(default=UNSET, alias="endpointServiceId")
    """Unique identifier of the interface endpoint you created in your VPC with the AWS(Service Name) or GCP(Target
    Service) resource"""


class OrganizationCloudRegionPrivateEndpointConfigDict(TypedDict):
    endpoint_service_id: NotRequired[str]
