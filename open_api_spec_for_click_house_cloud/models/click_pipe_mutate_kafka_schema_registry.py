from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_kafka_schema_registry_credentials import (
    ClickPipeKafkaSchemaRegistryCredentials,
    ClickPipeKafkaSchemaRegistryCredentialsDict,
)
from .enums.authentication import AuthenticationOrStr


class ClickPipeMutateKafkaSchemaRegistry(SdkBaseModel):
    url: Optional[str] = UNSET
    """Schema URL. HTTPS required."""

    authentication: Optional[AuthenticationOrStr] = UNSET
    """Authentication type of the schema registry."""

    ca_certificate: OptionalNullable[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificates to validate the schema registry's certificate."""

    credentials: Optional[ClickPipeKafkaSchemaRegistryCredentials] = UNSET


class ClickPipeMutateKafkaSchemaRegistryDict(TypedDict):
    url: NotRequired[str]
    authentication: NotRequired[AuthenticationOrStr]
    ca_certificate: NotRequired[str | None]
    credentials: NotRequired[ClickPipeKafkaSchemaRegistryCredentialsDict]
