from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_field_mapping import ClickPipeFieldMapping, ClickPipeFieldMappingDict
from .click_pipe_patch_destination import ClickPipePatchDestination, ClickPipePatchDestinationDict
from .click_pipe_patch_source import ClickPipePatchSource, ClickPipePatchSourceDict
from .click_pipe_settings import ClickPipeSettings, ClickPipeSettingsDict


class ClickPipePatchRequest(SdkBaseModel):
    name: OptionalNullable[str] = UNSET
    """Name of the ClickPipe."""

    source: OptionalNullable[ClickPipePatchSource] = UNSET
    destination: OptionalNullable[ClickPipePatchDestination] = UNSET
    field_mappings: Optional[list[ClickPipeFieldMapping]] = Field(default=UNSET, alias="fieldMappings")
    """Field mappings of the ClickPipe. This will not update the table schema, only the ClickPipe configuration."""

    settings: OptionalNullable[ClickPipeSettings] = UNSET


class ClickPipePatchRequestDict(TypedDict):
    name: NotRequired[str | None]
    source: NotRequired[ClickPipePatchSourceDict | None]
    destination: NotRequired[ClickPipePatchDestinationDict | None]
    field_mappings: NotRequired[list[ClickPipeFieldMappingDict]]
    settings: NotRequired[ClickPipeSettingsDict | None]
