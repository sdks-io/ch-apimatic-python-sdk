from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickStackMetricTables(SdkBaseModel):
    gauge: Optional[str] = UNSET
    """Table containing gauge metrics data"""

    histogram: Optional[str] = UNSET
    """Table containing histogram metrics data"""

    sum: Optional[str] = UNSET
    """Table containing sum metrics data"""

    summary: Optional[str] = UNSET
    """Table containing summary metrics data. Note - not yet fully supported by HyperDX"""

    exponential_histogram: Optional[str] = Field(default=UNSET, alias="exponential histogram")
    """Table containing exponential histogram metrics data. Note - not yet fully supported by HyperDX"""


class ClickStackMetricTablesDict(TypedDict):
    gauge: NotRequired[str]
    histogram: NotRequired[str]
    sum: NotRequired[str]
    summary: NotRequired[str]
    exponential_histogram: NotRequired[str]
