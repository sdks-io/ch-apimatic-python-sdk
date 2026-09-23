from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Color(str, Enum):
    """Optional palette-token override for the sparkline. When unset the sparkline inherits the tile's static color."""

    CHART_BLUE = "chart-blue"
    CHART_ORANGE = "chart-orange"
    CHART_RED = "chart-red"
    CHART_CYAN = "chart-cyan"
    CHART_GREEN = "chart-green"
    CHART_PINK = "chart-pink"
    CHART_PURPLE = "chart-purple"
    CHART_LIGHT_BLUE = "chart-light-blue"
    CHART_BROWN = "chart-brown"
    CHART_GRAY = "chart-gray"
    CHART_SUCCESS = "chart-success"
    CHART_WARNING = "chart-warning"
    CHART_ERROR = "chart-error"

    __str__ = str.__str__


ColorOrStr: TypeAlias = Annotated[Color | str, open_enum_validator(Color)]
