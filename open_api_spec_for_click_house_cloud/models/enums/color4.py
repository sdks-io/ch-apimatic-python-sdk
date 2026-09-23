from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Color4(str, Enum):
    """Optional static color applied to the displayed number."""

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


Color4OrStr: TypeAlias = Annotated[Color4 | str, open_enum_validator(Color4)]
