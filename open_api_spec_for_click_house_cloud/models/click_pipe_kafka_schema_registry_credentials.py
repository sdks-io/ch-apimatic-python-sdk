from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClickPipeKafkaSchemaRegistryCredentials(SdkBaseModel):
    username: Optional[str] = UNSET
    """Username for the schema registry."""

    password: Optional[str] = UNSET
    """Password for the schema registry."""


class ClickPipeKafkaSchemaRegistryCredentialsDict(TypedDict):
    username: NotRequired[str]
    password: NotRequired[str]
