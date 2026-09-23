from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .click_pipe_destination import ClickPipeDestination, ClickPipeDestinationDict
from .click_pipe_field_mapping import ClickPipeFieldMapping, ClickPipeFieldMappingDict
from .click_pipe_scaling import ClickPipeScaling, ClickPipeScalingDict
from .click_pipe_settings import ClickPipeSettings, ClickPipeSettingsDict
from .click_pipe_source import ClickPipeSource, ClickPipeSourceDict
from .enums.state2 import State2OrStr


class ClickPipe(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique ClickPipe ID."""

    service_id: Optional[UUID] = Field(default=UNSET, alias="serviceId")
    """ID of the service this ClickPipe belongs to."""

    name: Optional[str] = UNSET
    """Name of the ClickPipe."""

    state: Optional[State2OrStr] = UNSET
    """Current lifecycle state of the ClickPipe. For database pipes: "Provisioning" (initial setup), "Setup"
    (configuring replication), "Snapshot" (initial data load), "Running" (actively replicating), "Pausing"
    (transitioning to paused state), "Paused" (temporarily paused), "Modifying" (applying configuration updates),
    "Resync" (swapping resync tables with original tables), "Failed" (error occurred), "Unknown". For streaming/object
    storage pipes (Kafka, Kinesis, S3): "Unknown" (initial state), "Provisioning" (setting up resources), "Running"
    (actively ingesting data), "Stopping" (transitioning to stopped state), "Stopped" (manually stopped, can be
    restarted), "Completed" (batch ingestion finished for object storage), "Failed" (error occurred, pipe stopped),
    "InternalError" (internal system error)."""

    scaling: Optional[ClickPipeScaling] = UNSET
    source: Optional[ClickPipeSource] = UNSET
    destination: Optional[ClickPipeDestination] = UNSET
    field_mappings: Optional[list[ClickPipeFieldMapping]] = Field(default=UNSET, alias="fieldMappings")
    """Field mappings of the ClickPipe. Note that all destination columns must be included in the mappings."""

    settings: Optional[ClickPipeSettings] = UNSET
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Creation timestamp of the ClickPipe in ISO 8601 format."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Last update timestamp of the ClickPipe in ISO 8601 format."""


class ClickPipeDict(TypedDict):
    id: NotRequired[UUID]
    service_id: NotRequired[UUID]
    name: NotRequired[str]
    state: NotRequired[State2OrStr]
    scaling: NotRequired[ClickPipeScalingDict]
    source: NotRequired[ClickPipeSourceDict]
    destination: NotRequired[ClickPipeDestinationDict]
    field_mappings: NotRequired[list[ClickPipeFieldMappingDict]]
    settings: NotRequired[ClickPipeSettingsDict]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
