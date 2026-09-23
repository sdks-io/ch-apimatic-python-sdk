from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HeatmapScaleType(str, Enum):
    """Scale type used to bucket values on the y-axis."""

    LOG = "log"
    LINEAR = "linear"

    __str__ = str.__str__


HeatmapScaleTypeOrStr: TypeAlias = Annotated[HeatmapScaleType | str, open_enum_validator(HeatmapScaleType)]
