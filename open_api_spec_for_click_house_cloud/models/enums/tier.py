from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Tier(str, Enum):
    """DEPRECATED for BASIC, SCALE and ENTERPRISE organization tiers. Use ``minReplicaMemoryGb``,
    ``maxReplicaMemoryGb``, and ``numReplicas`` instead. Tier of the service: 'development', 'production',
    'dedicated_high_mem', 'dedicated_high_cpu', 'dedicated_standard', 'dedicated_standard_n2d_standard_4',
    'dedicated_standard_n2d_standard_8', 'dedicated_standard_n2d_standard_32', 'dedicated_standard_n2d_standard_128',
    'dedicated_standard_n2d_standard_32_16SSD', 'dedicated_standard_n2d_standard_64_24SSD'. Production services scale,
    Development are fixed size. Azure services don't support Development tier"""

    DEVELOPMENT = "development"
    PRODUCTION = "production"
    DEDICATED_HIGH_MEM = "dedicated_high_mem"
    DEDICATED_HIGH_CPU = "dedicated_high_cpu"
    DEDICATED_STANDARD = "dedicated_standard"
    DEDICATED_STANDARD_N2D_STANDARD_4 = "dedicated_standard_n2d_standard_4"
    DEDICATED_STANDARD_N2D_STANDARD_8 = "dedicated_standard_n2d_standard_8"
    DEDICATED_STANDARD_N2D_STANDARD_32 = "dedicated_standard_n2d_standard_32"
    DEDICATED_STANDARD_N2D_STANDARD_128 = "dedicated_standard_n2d_standard_128"
    DEDICATED_STANDARD_N2D_STANDARD_32_16_SSD = "dedicated_standard_n2d_standard_32_16SSD"
    DEDICATED_STANDARD_N2D_STANDARD_64_24_SSD = "dedicated_standard_n2d_standard_64_24SSD"

    __str__ = str.__str__


TierOrStr: TypeAlias = Annotated[Tier | str, open_enum_validator(Tier)]
