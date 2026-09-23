from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_destination_column import ClickPipeDestinationColumn, ClickPipeDestinationColumnDict


class ClickPipePatchDestination(SdkBaseModel):
    columns: Optional[list[ClickPipeDestinationColumn]] = UNSET
    """Columns of the destination table. This will not update the table schema, only the ClickPipe configuration."""


class ClickPipePatchDestinationDict(TypedDict):
    columns: NotRequired[list[ClickPipeDestinationColumnDict]]
