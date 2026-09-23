from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_field_mapping import ClickPipeFieldMapping, ClickPipeFieldMappingDict
from .click_pipe_mutate_destination import ClickPipeMutateDestination, ClickPipeMutateDestinationDict
from .click_pipe_post_source import ClickPipePostSource, ClickPipePostSourceDict
from .click_pipe_scaling import ClickPipeScaling, ClickPipeScalingDict
from .click_pipe_settings import ClickPipeSettings, ClickPipeSettingsDict


class ClickPipePostRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the ClickPipe."""

    source: Optional[ClickPipePostSource] = UNSET
    destination: Optional[ClickPipeMutateDestination] = UNSET
    field_mappings: Optional[list[ClickPipeFieldMapping]] = Field(default=UNSET, alias="fieldMappings")
    """Field mappings of the ClickPipe. Note that all destination columns must be included in the mappings."""

    scaling: Optional[ClickPipeScaling] = UNSET
    settings: Optional[ClickPipeSettings] = UNSET
    start_paused: Optional[bool] = Field(default=UNSET, alias="startPaused")
    """Create the ClickPipe in the Stopped state instead of starting ingestion immediately. Start it later with the
    state endpoint. Not supported for database ClickPipes."""


class ClickPipePostRequestDict(TypedDict):
    name: NotRequired[str]
    source: NotRequired[ClickPipePostSourceDict]
    destination: NotRequired[ClickPipeMutateDestinationDict]
    field_mappings: NotRequired[list[ClickPipeFieldMappingDict]]
    scaling: NotRequired[ClickPipeScalingDict]
    settings: NotRequired[ClickPipeSettingsDict]
    start_paused: NotRequired[bool]
