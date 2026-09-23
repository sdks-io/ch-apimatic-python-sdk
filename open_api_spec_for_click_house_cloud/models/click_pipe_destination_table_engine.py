from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.type11 import Type11OrStr


class ClickPipeDestinationTableEngine(SdkBaseModel):
    type_: Optional[Type11OrStr] = Field(default=UNSET, alias="type")
    """Engine type of the destination table."""

    version_column_id: OptionalNullable[str] = Field(default=UNSET, alias="versionColumnId")
    """Column name to use as version for ReplacingMergeTree engine."""

    column_ids: Optional[list[str]] = Field(default=UNSET, alias="columnIds")
    """Column names to sum for SummingMergeTree engine."""


class ClickPipeDestinationTableEngineDict(TypedDict):
    type_: NotRequired[Type11OrStr]
    version_column_id: NotRequired[str | None]
    column_ids: NotRequired[list[str]]
