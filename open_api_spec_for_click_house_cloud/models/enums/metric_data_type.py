from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MetricDataType(str, Enum):
    """Metric data type, only for metrics data sources."""

    SUM = "sum"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"
    EXPONENTIAL_HISTOGRAM = "exponential histogram"

    __str__ = str.__str__


MetricDataTypeOrStr: TypeAlias = Annotated[MetricDataType | str, open_enum_validator(MetricDataType)]
