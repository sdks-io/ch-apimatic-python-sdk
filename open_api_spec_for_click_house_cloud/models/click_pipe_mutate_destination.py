from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_destination_column import ClickPipeDestinationColumn, ClickPipeDestinationColumnDict
from .click_pipe_destination_table_definition import (
    ClickPipeDestinationTableDefinition,
    ClickPipeDestinationTableDefinitionDict,
)


class ClickPipeMutateDestination(SdkBaseModel):
    database: Optional[str] = UNSET
    """Destination database."""

    table: Optional[str] = UNSET
    """Destination table. Required field for all pipe types except database pipes (Postgres, MySQL, BigQuery)."""

    managed_table: Optional[bool] = Field(default=UNSET, alias="managedTable")
    """Is the table managed by ClickPipes? Required field for all pipe types except database pipes (Postgres, MySQL,
    BigQuery)."""

    table_definition: Optional[ClickPipeDestinationTableDefinition] = Field(default=UNSET, alias="tableDefinition")
    columns: Optional[list[ClickPipeDestinationColumn]] = UNSET
    """Columns of the destination table. Required field for all pipe types except database pipes (Postgres, MySQL,
    BigQuery)."""

    roles: Optional[list[str]] = UNSET
    """Optional. Roles to grant to the ClickHouse user that ClickPipe creates. If omitted, the user is granted the
    default role (``default_role``). Add your custom roles here if required. The role names ``clickpipes`` and
    ``clickpipes_system`` are reserved for internal use and cannot be assigned."""


class ClickPipeMutateDestinationDict(TypedDict):
    database: NotRequired[str]
    table: NotRequired[str]
    managed_table: NotRequired[bool]
    table_definition: NotRequired[ClickPipeDestinationTableDefinitionDict]
    columns: NotRequired[list[ClickPipeDestinationColumnDict]]
    roles: NotRequired[list[str]]
