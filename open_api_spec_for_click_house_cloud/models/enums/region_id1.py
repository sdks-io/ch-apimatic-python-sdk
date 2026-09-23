from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RegionId1(str, Enum):
    """Region in which the BYOC infrastructure will be located"""

    AP_NORTHEAST_1 = "ap-northeast-1"
    AP_NORTHEAST_2 = "ap-northeast-2"
    AP_SOUTH_1 = "ap-south-1"
    AP_SOUTHEAST_1 = "ap-southeast-1"
    AP_SOUTHEAST_2 = "ap-southeast-2"
    CA_CENTRAL_1 = "ca-central-1"
    EU_CENTRAL_1 = "eu-central-1"
    EU_WEST_1 = "eu-west-1"
    EU_WEST_2 = "eu-west-2"
    IL_CENTRAL_1 = "il-central-1"
    US_EAST_1 = "us-east-1"
    US_EAST_2 = "us-east-2"
    US_WEST_2 = "us-west-2"
    US_EAST1 = "us-east1"
    US_CENTRAL1 = "us-central1"
    EUROPE_WEST2 = "europe-west2"
    EUROPE_WEST4 = "europe-west4"
    ASIA_SOUTHEAST1 = "asia-southeast1"
    ASIA_NORTHEAST1 = "asia-northeast1"
    EASTUS = "eastus"
    EASTUS2 = "eastus2"
    WESTUS3 = "westus3"
    GERMANYWESTCENTRAL = "germanywestcentral"
    CENTRALUS = "centralus"

    __str__ = str.__str__


RegionId1OrStr: TypeAlias = Annotated[RegionId1 | str, open_enum_validator(RegionId1)]
