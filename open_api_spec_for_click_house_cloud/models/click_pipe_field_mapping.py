from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickPipeFieldMapping(SdkBaseModel):
    source_field: Optional[str] = Field(default=UNSET, alias="sourceField")
    """Source field name."""

    destination_field: Optional[str] = Field(default=UNSET, alias="destinationField")
    """Destination field name."""


class ClickPipeFieldMappingDict(TypedDict):
    source_field: NotRequired[str]
    destination_field: NotRequired[str]
