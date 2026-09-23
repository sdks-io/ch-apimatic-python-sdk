from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_destination_table_engine import ClickPipeDestinationTableEngine, ClickPipeDestinationTableEngineDict


class ClickPipeDestinationTableDefinition(SdkBaseModel):
    engine: Optional[ClickPipeDestinationTableEngine] = UNSET
    sorting_key: Optional[list[str]] = Field(default=UNSET, alias="sortingKey")
    """Sorting key of the destination table. List of columns."""

    partition_by: Optional[str] = Field(default=UNSET, alias="partitionBy")
    """Partition key SQL expression."""

    primary_key: Optional[str] = Field(default=UNSET, alias="primaryKey")
    """Primary key of SQL expression."""

    ttl: Optional[str] = UNSET
    """TTL SQL expression of the destination table."""


class ClickPipeDestinationTableDefinitionDict(TypedDict):
    engine: NotRequired[ClickPipeDestinationTableEngineDict]
    sorting_key: NotRequired[list[str]]
    partition_by: NotRequired[str]
    primary_key: NotRequired[str]
    ttl: NotRequired[str]
