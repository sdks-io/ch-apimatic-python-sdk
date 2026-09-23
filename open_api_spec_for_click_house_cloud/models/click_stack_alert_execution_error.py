from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.type15 import Type15OrStr


class ClickStackAlertExecutionError(SdkBaseModel):
    timestamp: RFC3339DateTime
    """When the error occurred."""

    type_: Type15OrStr = Field(alias="type")
    """Category of the error."""

    message: str
    """Human-readable error message."""


class ClickStackAlertExecutionErrorDict(TypedDict):
    timestamp: RFC3339DateTime
    type_: Type15OrStr
    message: str
