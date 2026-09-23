from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AzureEventHub(SdkBaseModel):
    connection_string: Optional[str] = Field(default=UNSET, alias="connectionString")
    """Connection string for Azure EventHub source."""


class AzureEventHubDict(TypedDict):
    connection_string: NotRequired[str]
