from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UdfArgumentOutput(SdkBaseModel):
    name: str
    """Name of the argument. Required for Native and JSONEachRow formats."""

    type_: str = Field(alias="type")
    """ClickHouse data type of the argument."""


class UdfArgumentOutputDict(TypedDict):
    name: str
    type_: str
