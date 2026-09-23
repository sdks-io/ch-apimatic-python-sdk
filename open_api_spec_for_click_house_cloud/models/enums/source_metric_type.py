from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SourceMetricType(str, Enum):
    """Metric type when source is metrics"""

    SUM = "sum"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"
    EXPONENTIAL_HISTOGRAM = "exponential histogram"

    __str__ = str.__str__


SourceMetricTypeOrStr: TypeAlias = Annotated[SourceMetricType | str, open_enum_validator(SourceMetricType)]
