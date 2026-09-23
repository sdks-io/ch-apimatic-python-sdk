from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MetricType(str, Enum):
    """Metric type; only applicable when the source is a metrics source."""

    SUM = "sum"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"
    EXPONENTIAL_HISTOGRAM = "exponential histogram"

    __str__ = str.__str__


MetricTypeOrStr: TypeAlias = Annotated[MetricType | str, open_enum_validator(MetricType)]
