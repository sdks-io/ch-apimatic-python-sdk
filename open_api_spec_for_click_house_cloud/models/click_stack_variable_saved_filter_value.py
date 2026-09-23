from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackVariableSavedFilterValue(SdkBaseModel):
    type_: Literal["variable"] = Field(default="variable", alias="type")
    """Filter type."""

    name: str
    """The variableName of the dashboard variable this selection belongs to. Only allowed for variable-enabled
    filters."""

    values: list[str]
    """Selected values"""


class ClickStackVariableSavedFilterValueDict(TypedDict):
    type_: Literal["variable"]
    name: str
    values: list[str]
